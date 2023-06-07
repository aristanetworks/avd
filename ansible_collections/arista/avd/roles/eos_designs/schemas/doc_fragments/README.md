Files and folders in this directory or subdirectories are read by the template "avd_schema_documentation.j2".

Directory and file layout and naming convention:

- `doc_fragments/<documentation filename including .md>`:
  Markdown rendered directly under the level-1 heading at the top of the file matching the name of the fragment.

- `doc_fragments/<documentation filename excluding .md>/<section_name>.md`:
  Markdown rendered rendered directly under the level-2 heading of the section matching the name of the fragment.

- `doc_fragments/<documentation filename excluding .md>/<section_name>/<table_name>.md`:
- Fragments under the "tables" directory are rendered directly under the level-3 heading of the table matching the name of the fragment.

NOTE: All directory and file names are case sensitive.

NOTE: For generated files placed in subfolders under docs, the fragments must be placed in similar subfolders here.
