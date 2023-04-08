#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = matrix[:]
    square_matrix = []
    for row in copy_matrix:
        square_row = []
        for val in row:
            square_row.append(val ** 2)
            square_matrix.append(square_row)
            return square_matrix
