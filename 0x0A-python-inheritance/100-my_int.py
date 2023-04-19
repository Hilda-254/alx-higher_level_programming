#!/usr/bin/python3
"""A class MyInt that inherits from int"""


class MyInt(int):
    """A class MyInt that inherits from int"""
    def __eq__(self, other):
        """Overide and return opposite of result"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return the opposite of the result"""
        return super().__eq__(other)
