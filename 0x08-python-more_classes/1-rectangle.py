#!/usr/bin/python3
# 1-rectangle.py by HILDA MUNJURI
"""A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width:The width of the rectangle.
            height:The height of the rectangle.
        Raises:
            TypeError: If value is not integer
            ValueError: If value is less than zero
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    Rectangle = property(width, height)
