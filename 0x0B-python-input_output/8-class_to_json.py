#!/usr/bin/python3
""" A function that returns the dictionary description with
simple data structure or JSON serialization"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure."""
    return obj.__dict__
