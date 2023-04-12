#!/usr/bin/python3
# 5-square.py by HILDA MUNJURI
"""A class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initialize square class
        Args: size - the size of the defined square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Retrieve size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
