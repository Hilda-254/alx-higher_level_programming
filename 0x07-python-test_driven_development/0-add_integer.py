#!/usr/bin/python3
# 0-add_integer.py by HILDA MUNJURI
"""A  function that adds 2 integers"""


def add_integer(a, b=98):
    """Returns the sum of two integers or floats as integers
    Args:
        a: first argument
        b: second argument
    Returns:
        Sum of the two arguments
    Raises:
        TypeError: If arguments are not an integer or a float
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
