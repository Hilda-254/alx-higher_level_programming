#!/usr/bin/python3
"""A class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """Base of surface on which a shape stands on."""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
