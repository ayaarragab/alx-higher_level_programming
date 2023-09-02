#!/bin/usr/python3
"""
This module contains a function that
prints a square with the character
print_square(size): prints a square of size size
"""
def print_square(size):
    """
    print_square(size):prints a square of size # 
    """
    if (size == "" or not isinstance(size, int) or
        (isinstance(size, float) and size < 0)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    pattern = size * '#'
    for i in range(size):
        print(pattern)
