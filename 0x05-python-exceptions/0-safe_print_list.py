#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i, num in enumerate(my_list):
        count += 1
        try:
            print(my_list[i], end="")
        except IndexError:
            break
    print()
    return count
