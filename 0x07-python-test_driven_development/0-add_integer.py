#!/usr/bin/python3
"""
add_integer
This module consists of an add function
Functions: add(a, b): returns sum of two numbers
"""


def add_integer(a, b=98):
    """ :param a: first arg :param b: second arg
    :return: a + b
    """
    if not type(a) in (int, float):
        raise TypeError('a must be an integer')
    if not type(b) in (int, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
