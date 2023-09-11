#!/usr/bin/python3
"""
This module for a class Rectangle that inherits
from BaseGeometry (7-base_geometry.py).
"""


class BaseGeometry:
    """an empty class BaseGeometry.
    """
    def area(self):
        """area
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator
        """
        if not type(value) is int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """
    rec class
    """
    def __init__(self, width, height):
        """
        Initialization of Rectangle object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = width
