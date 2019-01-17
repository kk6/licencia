import sys

from cleo import Command
from pip._internal.commands.show import search_packages_info

from .core import create_table
from .core import get_package_names
from .core import load_toml


class ListCommand(Command):
    """
    List the licenses for external packages used in your repository.

    list
    """

    def handle(self):
        try:
            pyproject = load_toml("poetry.lock")
        except FileNotFoundError:
            self.line_error("<error>The lock file not found.</error>")
            sys.exit(1)

        package_names = get_package_names(pyproject)
        if not package_names:
            self.line("No data")
            sys.exit(1)

        results = search_packages_info(package_names)
        rows = [(p["name"], p["license"]) for p in results]
        table = create_table(rows)
        print(table)
