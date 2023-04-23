#!/usr/bin/python3
"""A module that defines a class Student"""


class Student:
    """A class that represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
