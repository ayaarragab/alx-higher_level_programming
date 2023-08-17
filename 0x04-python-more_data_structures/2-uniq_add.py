#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    sum = 0
    for num in my_list:
        my_set.add(num)
    for num in my_set:
        sum += num
    return (sum)
