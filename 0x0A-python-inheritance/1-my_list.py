#!/usr/bin/python3
"""Module that inherits list and prints in ascending order"""


class MyList(list):
    """A class MyList that inherits from list."""

    def print_sorted(self):
        """Sorts and prints the list in ascending sort."""
        print(sorted(self))
