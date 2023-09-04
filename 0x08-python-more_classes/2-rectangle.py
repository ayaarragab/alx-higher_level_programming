#!/usr/bin/python3
"""rectangle class module"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """__init__: an instance method that is called
        when a new object created"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter function"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter function"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
