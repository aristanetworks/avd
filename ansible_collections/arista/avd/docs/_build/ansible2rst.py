#!/usr/bin/env python
# (c) 2012, Jan-Piet Mens <jpmens () gmail.com>
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import re
import sys
import datetime
import cgi
import yaml
import logging
from distutils.version import LooseVersion
from jinja2 import Environment, FileSystemLoader
from ansible.module_utils.six import print_
from ansible.module_utils.common._collections_compat import MutableMapping, MutableSet, MutableSequence
from ansible.module_utils.six import iteritems, string_types
from ansible.parsing.plugin_docs import read_docstring
from ansible.parsing.yaml.loader import AnsibleLoader
from ansible.plugins.loader import fragment_loader
from ansible.module_utils._text import to_bytes
from ansible.errors import AnsibleError, AnsibleParserError

try:
    from html import escape as html_escape
except ImportError:
    # Python-3.2 or later
    import cgi

    def html_escape(text, quote=True):
        return cgi.escape(text, quote)

from ansible import __version__ as ansible_version

#####################################################################################
# constants and paths

# if a module is added in a version of Ansible older than this, don't print the version added information
# in the module documentation because everyone is assumed to be running something newer than this already.
TO_OLD_TO_BE_NOTABLE = 1.3

_ITALIC = re.compile(r"I\(([^)]+)\)")
_BOLD = re.compile(r"B\(([^)]+)\)")
_MODULE = re.compile(r"M\(([^)]+)\)")
_URL_W_TEXT = re.compile(r"U\(([^)^|]+)\|([^)]+)\)")
_URL = re.compile(r"U\(([^)^|]+)\)")
_CONST = re.compile(r"C\(([^)]+)\)")
_UNDERSCORE = re.compile(r"_")
DEPRECATED = b" (D)"

MODULE_NAME_STARTS_WITH = ""
MODULEDIR = "../../plugins/modules/"
OUTPUTDIR = "../"

#####################################################################################


def too_old(added):
    if not added:
        return False
    try:
        added_tokens = str(added).split(".")
        readded = added_tokens[0] + "." + added_tokens[1]
        added_float = float(readded)
    except ValueError as e:
        return False
    return added_float < TO_OLD_TO_BE_NOTABLE

#####################################################################################


def rst_ify(text):
    ''' convert symbols like I(this is in italics) to valid restructured text '''

    try:
        t = _ITALIC.sub(r'*' + r"\1" + r"*", text)
        t = _BOLD.sub(r'**' + r"\1" + r"**", t)
        t = _MODULE.sub(r':ref:`' + r"\1 <\1>" + r"`", t)
        t = _URL_W_TEXT.sub(r'`' + r"\1" + r" <" + r"\2" + r">`_", t)
        t = _URL.sub(r'`' + r"\1" + r" <" + r"\1" + r">`_", t)
        t = _CONST.sub(r'``' + r"\1" + r"``", t)
    except Exception as e:
        raise AnsibleError("Could not process (%s) : %s" % (str(text), str(e)))

    return t

#####################################################################################


def module_to_html(matchobj):
    if matchobj.group(1) is not None:
        module_name = matchobj.group(1)
        module_href = _UNDERSCORE.sub('-', module_name)
        return '<a class="reference internal" href="#' + module_href + '"><span class="std std-ref">' + \
            module_name + '</span></a>'
    return ''


def html_ify(text):
    ''' convert symbols like I(this is in italics) to valid HTML '''

    t = html_escape(text)
    t = _ITALIC.sub("<em>" + r"\1" + "</em>", t)
    t = _BOLD.sub("<b>" + r"\1" + "</b>", t)
    t = _MODULE.sub(module_to_html, t)
    t = _URL_W_TEXT.sub("<a href='" + r"\2" + "'>" + r"\1" + "</a>", t)
    t = _URL.sub("<a href='" + r"\1" + "'>" + r"\1" + "</a>", t)
    t = _CONST.sub("<code>" + r"\1" + "</code>", t)

    return t


#####################################################################################


def rst_fmt(text, fmt):
    ''' helper for Jinja2 to do format strings '''

    return fmt % (text)

#####################################################################################


def rst_xline(width, char="="):
    ''' return a restructured text line of a given length '''

    return char * width

#####################################################################################


def write_data(text, outputname, module, output_dir=None):
    ''' dumps module output to a file or the screen, as requested '''

    if output_dir is not None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        fname = os.path.join(output_dir, outputname % (module))
        with open(fname, 'wb') as f:
            f.write(to_bytes(text))
    else:
        print(text)

#####################################################################################


def jinja2_environment(template_dir, template_type):

    env = Environment(loader=FileSystemLoader(template_dir),
                      variable_start_string="@{",
                      variable_end_string="}@",
                      trim_blocks=True,
                      )
    env.globals['xline'] = rst_xline

    if template_type == 'rst':
        env.filters['convert_symbols_to_format'] = rst_ify
        env.filters['html_ify'] = html_ify
        env.filters['fmt'] = rst_fmt
        env.filters['xline'] = rst_xline
        template = env.get_template('rst.j2')
        outputname = "%s.rst"
    else:
        raise Exception("unknown module format type: %s" % template_type)

    return env, template, outputname

#####################################################################################


def add_fragments(doc, filename):

    fragments = doc.get('extends_documentation_fragment', [])

    if isinstance(fragments, string_types):
        fragments = [fragments]

    # Allow the module to specify a var other than DOCUMENTATION
    # to pull the fragment from, using dot notation as a separator
    for fragment_slug in fragments:
        fragment_slug = fragment_slug.lower()
        if '.' in fragment_slug:
            fragment_name, fragment_var = fragment_slug.split('.', 1)
            fragment_var = fragment_var.upper()
        else:
            fragment_name, fragment_var = fragment_slug, 'DOCUMENTATION'

        fragment_loader.add_directory('../../plugins/modules/')
        fragment_class = fragment_loader.get(fragment_name)
        assert fragment_class is not None

        fragment_yaml = getattr(fragment_class, fragment_var, '{}')
        fragment = AnsibleLoader(
            fragment_yaml, file_name=filename).get_single_data()

        if 'notes' in fragment:
            notes = fragment.pop('notes')
            if notes:
                if 'notes' not in doc:
                    doc['notes'] = []
                doc['notes'].extend(notes)

        if 'options' not in fragment and 'logging_options' not in fragment and 'connection_options' not in fragment:
            raise Exception("missing options in fragment (%s), possibly misformatted?: %s" % (
                fragment_name, filename))

        for key, value in iteritems(fragment):
            if key in doc:
                # assumes both structures have same type
                if isinstance(doc[key], MutableMapping):
                    value.update(doc[key])
                elif isinstance(doc[key], MutableSet):
                    value.add(doc[key])
                elif isinstance(doc[key], MutableSequence):
                    value = sorted(frozenset(value + doc[key]))
                else:
                    raise Exception("Attempt to extend a documentation fragement (%s) of unknown type: %s" % (
                        fragment_name, filename))
            doc[key] = value


def get_docstring(filename, verbose=False):
    """
    DOCUMENTATION can be extended using documentation fragments loaded by the PluginLoader from the module_docs_fragments directory.
    """

    data = read_docstring(filename, verbose=verbose)

    # add fragments to documentation
    if data.get('doc', False):
        add_fragments(data['doc'], filename)

    return data['doc'], data['plainexamples'], data['returndocs'], data['metadata']


def process_module(fname, template, outputname, aliases=None):

    module_name = fname.replace(".py", "")

    print_("Processing  module %s" % (MODULEDIR + fname))
    doc, examples, returndocs, metadata = get_docstring(MODULEDIR + fname,
                                                        verbose=True)

    # add some defaults for plugins that dont have most of the info
    doc['module'] = doc.get('module', module_name)
    doc['version_added'] = doc.get('version_added', 'historical')
    doc['plugin_type'] = 'module'

    required_fields = ('short_description',)
    for field in required_fields:
        if field not in doc:
            print_("%s: WARNING: MODULE MISSING field '%s'" % (fname, field))

    not_nullable_fields = ('short_description',)
    for field in not_nullable_fields:
        if field in doc and doc[field] in (None, ''):
            print_("%s: WARNING: MODULE field '%s' DOCUMENTATION is null/empty value=%s" %
                   (fname, field, doc[field]))

    #
    # The present template gets everything from doc so we spend most of this
    # function moving data into doc for the template to reference
    #

    if aliases:
        doc['aliases'] = aliases

    # don't show version added information if it's too old to be called out
    added = 0
    if doc['version_added'] == 'historical':
        del doc['version_added']
    else:
        added = doc['version_added']

    # Strip old version_added for the module
    if too_old(added):
        del doc['version_added']

    option_names = []
    if 'options' in doc and doc['options']:
        for (k, v) in iteritems(doc['options']):
            # Error out if there's no description
            if 'description' not in doc['options'][k]:
                raise AnsibleError(
                    "Missing required description for option %s in %s " % (k, module_name))

            # Error out if required isn't a boolean (people have been putting
            # information on when something is required in here.  Those need
            # to go in the description instead).
            required_value = doc['options'][k].get('required', False)
            if not isinstance(required_value, bool):
                raise AnsibleError("Invalid required value '%s' for option '%s' in '%s' (must be truthy)" % (
                    required_value, k, module_name))

            # Strip old version_added information for options
            if 'version_added' in doc['options'][k] and too_old(doc['options'][k]['version_added']):
                del doc['options'][k]['version_added']

            # Make sure description is a list of lines for later formatting
            if not isinstance(doc['options'][k]['description'], list):
                doc['options'][k]['description'] = [
                    doc['options'][k]['description']]
            option_names.append(k)
    option_names.sort()
    doc['option_keys'] = option_names

    connection_option_names = []
    if 'connection_options' in doc and doc['connection_options']:
        for (k, v) in iteritems(doc['connection_options']):
            # Error out if there's no description
            if 'description' not in doc['connection_options'][k]:
                raise AnsibleError(
                    "Missing required description for connection_option %s in %s " % (k, module_name))

            # Error out if required isn't a boolean (people have been putting
            # information on when something is required in here.  Those need
            # to go in the description instead).
            required_value = doc['connection_options'][k].get(
                'required', False)
            if not isinstance(required_value, bool):
                raise AnsibleError("Invalid required value '%s' for connection_option '%s' in '%s' (must be truthy)" %
                                   (required_value, k, module_name))

            # Strip old version_added information for options
            if ('version_added' in doc['connection_options'][k] and
                    too_old(doc['connection_options'][k]['version_added'])):
                del doc['connection_options'][k]['version_added']

            # Make sure description is a list of lines for later formatting
            if not isinstance(doc['connection_options'][k]['description'], list):
                doc['connection_options'][k]['description'] = [
                    doc['connection_options'][k]['description']]
            connection_option_names.append(k)
    connection_option_names.sort()
    doc['connection_option_keys'] = connection_option_names

    logging_option_names = []
    if 'logging_options' in doc and doc['logging_options']:
        for (k, v) in iteritems(doc['logging_options']):
            # Error out if there's no description
            if 'description' not in doc['logging_options'][k]:
                raise AnsibleError(
                    "Missing required description for logging_option %s in %s " % (k, module_name))

            # Error out if required isn't a boolean (people have been putting
            # information on when something is required in here.  Those need
            # to go in the description instead).
            required_value = doc['logging_options'][k].get('required', False)
            if not isinstance(required_value, bool):
                raise AnsibleError("Invalid required value '%s' for logging_option '%s' in '%s' (must be truthy)" %
                                   (required_value, k, module_name))

            # Strip old version_added information for options
            if ('version_added' in doc['logging_options'][k] and
                    too_old(doc['logging_options'][k]['version_added'])):
                del doc['logging_options'][k]['version_added']

            # Make sure description is a list of lines for later formatting
            if not isinstance(doc['logging_options'][k]['description'], list):
                doc['logging_options'][k]['description'] = [
                    doc['logging_options'][k]['description']]
            logging_option_names.append(k)
    logging_option_names.sort()
    doc['logging_option_keys'] = logging_option_names

    doc['filename'] = fname
    doc['docuri'] = doc['module'].replace('_', '-')
    doc['now_date'] = datetime.date.today().strftime('%Y-%m-%d')
    doc['ansible_version'] = ansible_version
    doc['plainexamples'] = examples  # plain text
    doc['metadata'] = metadata

    if returndocs:
        try:
            doc['returndocs'] = yaml.safe_load(returndocs)
            returndocs_keys = list(doc['returndocs'].keys())
            returndocs_keys.sort()
            doc['returndocs_keys'] = returndocs_keys
        except Exception as e:
            print_("%s:%s:yaml error:%s:returndocs=%s" %
                   (fname, module_name, e, returndocs))
            doc['returndocs'] = None
            doc['returndocs_keys'] = None
    else:
        doc['returndocs'] = None
        doc['returndocs_keys'] = None

    doc['author'] = doc.get('author', ['UNKNOWN'])
    if isinstance(doc['author'], string_types):
        doc['author'] = [doc['author']]

    # here is where we build the table of contents...
    text = template.render(doc)
    write_data(text, outputname, module_name, OUTPUTDIR)

#####################################################################################


def main():

    env, template, outputname = jinja2_environment('.', 'rst')
    module_names = []

    for module in os.listdir(MODULEDIR):
        if module.startswith(MODULE_NAME_STARTS_WITH):
            process_module(module, template, outputname)
            module_names.append(module.replace(".py", ""))

    index_file_path = os.path.join(OUTPUTDIR, "index.rst")
    index_file = open(index_file_path, "w")
    index_file.write('Arista Cloudvision Ansible Modules\n')
    index_file.write('==================================\n')
    index_file.write('\n')
    index_file.write('.. toctree::\n')
    index_file.write('  :caption: Project Documentation\n')
    index_file.write('  :name: mastertoc::\n')
    index_file.write('  :maxdepth: 1\n')
    index_file.write('\n')
    index_file.write('   Collection Overview <../README.md>\n')
    index_file.write('\n')
    index_file.write('.. toctree::\n')
    index_file.write('  :caption: Roles List\n')
    index_file.write('  :name: roletoc::\n')
    index_file.write('  :maxdepth: 1\n')
    index_file.write('\n')
    index_file.write(
        '   DHCP Configuration <../ansible_collections/arista/cvp/roles/dhcp_configuration/README.md>\n')
    index_file.write('\n')
    index_file.write('.. toctree::\n')
    index_file.write('  :caption: Modules List\n')
    index_file.write('  :name: moduletoc::\n')
    index_file.write('  :maxdepth: 1\n')
    index_file.write('\n')

    for module_name in module_names:
        index_file.write('   Module arista.cvp.%s <%s>\n' % (module_name, module_name))


if __name__ == '__main__':
    main()
