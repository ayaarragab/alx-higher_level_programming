#!/usr/bin/python3
"""
Rectangle class module
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle module
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method __init__
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Width setter
        """
        if not type(width) is int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height setter
        """
        if not type(height) is int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x setter
        """
        if not type(x) is int:
            raise TypeError('x must be an integer')
        if x <= 0:
            raise ValueError('x must be > 0')
        self.__x = x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        y setter
        """
        if not type(y) is int:
            raise TypeError('y must be an integer')
        if y <= 0:
            raise ValueError('y must be > 0')
        self.__y = y
