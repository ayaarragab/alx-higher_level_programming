#!/usr/bin/python3
"""This module defines square class with size attribute
with validation && with calculating area
"""


class Square:
    """This is a square class with size private attribute with validation
    && with calculating area"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._Square__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        return self.size * self.size
