#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)"""


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


class Rectangle(BaseGeometry):
    """A class that defines a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representation of a Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
