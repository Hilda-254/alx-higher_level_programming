#!/usr/bin/python3
"""A function that returns True if the object is exactly an
instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """Check if object is an instance of the specified class"""
    return (type(obj) == a_class)
