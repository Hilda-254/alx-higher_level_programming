#!/usr/bin/python3
# 2-square.py by HILDA MUNJURI
"""A class Square that defines a square by: (based on 1-square.py)"""


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
        else:
            self.__size = size
