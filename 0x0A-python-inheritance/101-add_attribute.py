#!/usr/bin/python3
"""A function that adds a new attribute to an object if possible"""


def add_new_attribute(obj, attr_name, attr_value):
    """A function that adds a new attribute to an object if possible
    Raise a TypeError exception, if the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
