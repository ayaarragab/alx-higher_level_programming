#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        my_list = []
    if idx in range(len(my_list)):
        del my_list[idx]
    return my_list
