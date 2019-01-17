import tomlkit
from beautifultable import BeautifulTable


def load_toml(filename):
    """
    Load toml file.

    :param filename: filename
    :return: toml body
    :rtype: dict

    """
    with open(filename) as f:
        return tomlkit.parse(f.read())


def get_package_names(pyproject):
    """
    Get package names

    :param dict pyproject: pyproject.toml body.
    :return: Package names
    :rtype: list

    """
    package_names = []
    for pkg in pyproject["package"]:
        if pkg["category"] == "main":
            package_names.append(pkg["name"])
    return package_names


def create_table(rows):
    """
    Create table for display

    :param list rows: table rows
    :return: table for display
    :rtype: BeautifulTable

    """
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.column_headers = ["name", "license"]
    table.column_alignments["name"] = BeautifulTable.ALIGN_LEFT
    table.column_alignments["license"] = BeautifulTable.ALIGN_LEFT
    for row in rows:
        table.append_row(row)
    return table
