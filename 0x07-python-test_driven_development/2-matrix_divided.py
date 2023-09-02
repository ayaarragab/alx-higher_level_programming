#!/usr/bin/python3
"""
This module contains a function that divides a matrix
matrix_divided - divides a matrix by number div
isFloatOrInt(num): returns True if num is int or float and false if other
"""


def isFloatOrInt(num):
    """
    isFloatOrInt(num): returns True if num is int or float and false if other
    """
    if not type(num) in (int, float):
        return False
    return True


def matrix_divided(matrix, div):
    """ matrix_divided(matrix, div): Returns new matrix
    with each value divided by div
    """
    if not matrix or not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists)\
        of integers/floats')
    if not type(div) in (int, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    for row_w in matrix:
        if not isinstance(row_w, list):
            raise TypeError('matrix must be a matrix (list of lists)\
        of integers/floats')
    for row in matrix:
        for num in row:
            if isFloatOrInt(num):
                continue
            raise TypeError('matrix must be a matrix (list of lists)\
            of integers/floats')
    currentRow = matrix[0]
    for roww in matrix:
        if len(currentRow) != len(roww):
            raise TypeError('Each row of the matrix must have the same size')
    newList = list(map(lambda myrow:
                       list(map(lambda x: round(x / div, 2), myrow)), matrix))
    return newList
