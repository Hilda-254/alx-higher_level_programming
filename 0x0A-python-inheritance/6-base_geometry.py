#!/usr/bin/python3
"""A class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry:
    """Base of surface on which a shape stands on."""

    def area(self):
        """Not used"""
        raise Exception("area() is not implemented")
