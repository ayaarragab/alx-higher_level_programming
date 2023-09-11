#!/usr/bin/python3
"""Inheris from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    """
    def __init__(self, size):
        """init
        method
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area
        method"""
        return self.__size * self.__size

    def __str__(self):
        """special method called when print()/ str() an object"""
        return f"[Square] {self.__size}/{self.__size}"
