#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda myrow: list(map(lambda x: x * x, myrow)), matrix))
