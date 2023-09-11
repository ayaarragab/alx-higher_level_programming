#!/usr/bin/python3
"""
This module for a class Rectangle that inherits
from other class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rec class
    """


    def __init__(self, width, height):
        """
        Initialization of Rectangle object
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = width
