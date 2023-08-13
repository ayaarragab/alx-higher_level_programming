#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        my_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    backup = my_list.copy()
    backup[idx] = element
    return backup
