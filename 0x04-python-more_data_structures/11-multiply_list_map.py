#!/usr/bin/python3
def mul_2(num):
    return num * 2


def multiply_list_map(my_list=[], number=0):
    new_list = map(mul_2, my_list)
    return list(new_list)
