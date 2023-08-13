#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max = my_list[0]
        i = 0
        while i < len(my_list) - 1:
            if my_list[i + 1] > max:
                max = my_list[i + 1]
            i += 1
        return max
