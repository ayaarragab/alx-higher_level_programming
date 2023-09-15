#!/usr/bin/python3
"""
module about function
returns a list of lists of integers
representing the Pascal triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal triangle of n
    """

    lists = [] * n
    for i in range(n):
        lists.append([0]*i)   # Fill list of lists by n lists, from 1 to n
    # each one has length of its order

    for list in lists:
        list.insert(0, 1)
        if len(list) > 1:
            list[-1] = 1
    for i in range(2, n):
        for j in range(1, i):
            lists[i][j] = lists[i-1][j-1] + lists[i-1][j]
            # each item = item of prev list + the item next to it
    return lists
