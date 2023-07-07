from html import escape
from pathlib import Path
from sys import path

from yaml import safe_dump

REPO_PATH = str(Path(__file__).parents[5])
path.append(REPO_PATH)

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdtodocumentationschemaconverter import AvdToDocumentationSchemaConverter

TABLES = {}


def on_pre_build(config, **kwargs):
    for schema_id in ["eos_cli_config_gen", "eos_designs"]:
        schema = AvdSchema(schema_id=schema_id)
        TABLES[schema_id] = AvdToDocumentationSchemaConverter(schema).convert_schema_to_tables()


def indent_text(text: str, indent: int, first_line: bool) -> str:
    indentation = " " * indent
    lines = str(text).splitlines()
    indented_lines = f"\n{indentation}".join(lines)
    if first_line:
        indented_lines = indentation + indented_lines

    return indented_lines


def build_table(schema_id: str, table_name: str) -> str:
    table = TABLES[schema_id][table_name]
    annotations = {}
    output = """
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
"""
    for row_index, row in enumerate(table["table"]):
        variable = escape(row["variable"])
        variable_text = str(variable).replace("  ", "&nbsp;&nbsp;")
        if (default_value := row.get("default")) is not None:
            if str(row["type"]).startswith(("List", "Dictionary")) and len(default_value) > 1:
                annotations[row_index] = safe_dump({str(variable).strip(): default_value})
                default_value = "See (+) on YAML tab"
            else:
                default_value = f"`{default_value}`"

        deprecation_label = ""
        if deprecation := row.get("deprecation", ""):
            deprecation = f"""<span style="color:red">{deprecation}</span>"""
            deprecation_label = f""" <span style="color:red">{row["deprecation_label"]}</span>"""

        table_cells = [
            f"""[<samp>{variable_text}</samp>](## "{escape(row["var_path"])}"){deprecation_label}""",
            row["type"],
            row.get("required", ""),
            default_value or "",
            row.get("restrictions", ""),
            f"""{row.get("description", "")}{deprecation}""",
        ]

        output += f"""    | {" | ".join(str(table_cell) for table_cell in table_cells)} |\n"""

    output += """
=== "YAML"

    ```yaml
"""
    annotation_counter = 0
    for row_index, row in enumerate(table["yaml"]):
        if row_index in annotations:
            annotation_counter += 1
            output += f"    {row} # ({annotation_counter})!\n"
        else:
            output += f"    {row}\n"

    output += "    ```\n"

    if annotations:
        output += "\n"
        for annotation_index, annotation in enumerate(annotations.values()):
            output += f"""    {annotation_index + 1}. Default Value:\n\n        ```yaml\n"""
            output += indent_text(annotation, 8, True)
            output += "\n        ```\n"

    return output


def on_page_markdown(markdown: str, *args, **kwargs):
    TAG = "--avdschema--"
    if TAG not in markdown:
        return

    IDENTIFIER_SEPERATOR = ":"
    starttag = markdown.find(TAG)
    endtag = markdown.find(TAG, starttag + len(TAG))

    while starttag >= 0 and endtag >= 0:
        identifier = markdown[starttag + len(TAG) : endtag].strip("\n\t ")
        if IDENTIFIER_SEPERATOR in identifier:
            schema_id, table_name = identifier.split(IDENTIFIER_SEPERATOR, maxsplit=1)
            markdown = markdown[:starttag] + build_table(schema_id=schema_id, table_name=table_name) + markdown[endtag + len(TAG) :]

        starttag = markdown.find(TAG)
        endtag = markdown.find(TAG, starttag + len(TAG))

    return markdown
