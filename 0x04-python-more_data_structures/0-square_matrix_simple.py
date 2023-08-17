#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = list()
        for list_ in matrix:
            single_list = list()
            for number in list_:
                single_list.append(number ** 2)
            new_matrix.append(single_list)
        return new_matrix
    else:
        return None
