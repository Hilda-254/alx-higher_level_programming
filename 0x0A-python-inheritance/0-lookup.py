#!/usr/bin/python3
"""Lists available attributes and methods using lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return (dir(obj))
