#!/usr/bin/python3
"""
This module contains the function matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    
    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.
    
    Returns:
        list of lists of float: A new matrix with each element divided by div.
    
    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix
    if (
        not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ele, (int, float)) for row in matrix for ele in row)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Validate row size consistency
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    return [[round(ele / div, 2) for ele in row] for row in matrix]
