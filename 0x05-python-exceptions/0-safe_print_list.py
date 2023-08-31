#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i, num in enumerate(my_list):
        try:
            print(my_list[i], end="")
        except IndexError:
            continue
    print()
    return i + 1
