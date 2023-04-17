#!/usr/bin/python3
"""This module defines a matrix division function
"""


def matrix_divided(matrix, div):
    """This function divides all the elements of a matrix by a given number
    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If the matrix has non-numbers
        TypeError: If the matrix has rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
    """
    if not all(isinstance(row, list) for row in matrix) or
    not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(num/div, 2) for num in row] for row in matrix]
    return new_matrix
