#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_one = list()
    for i, num in enumerate(my_list):
        if num == search:
            new_one.append(replace)
        else:
            new_one.append(num)
    return new_one
