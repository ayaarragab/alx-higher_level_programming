#!/usr/bin/python3
def no_c(my_string):
    newOne = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        newOne += i
    return newOne
