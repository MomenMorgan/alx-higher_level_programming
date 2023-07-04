#!/usr/bin/python3
"""
Divides each element of the matrix
"""


def matrix_divided(matrix, div):
    """divides the list of int or float
    Args:
        matrix list of lists (int or float)
        div (int or float): divisor
    Returns:
        a new list of lists containing the result
    """
    mat = []

    if div is None or type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        mat_s = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int\
               and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            if len(matrix[0]) != len(matrix[i]):
                raise TypeError("Each row of the matrix"
                                " must have the same size")
            mat_s.append(round((matrix[i][j]) / div, 2))
        mat.append(mat_s)
    return mat
