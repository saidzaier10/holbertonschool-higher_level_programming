#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
