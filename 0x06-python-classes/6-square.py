#!/usr/bin/python3
"""This module defines square class with size attribute
with validation && with calculating area && printing the square
&& considring the position
"""


class Square:
    """This is a square class with size private attribute with validation
    && with calculating area && printing the square
    && considring the position"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0 or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self._position = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        pattern = '#' * self.size
        spacePatter = ' ' * self.position[0]
        if self.size == 0:
            print()
        for newline in range(self.position[1]):
            print()
        for i in range(self.size):
            if i == self.size:
                print(spacePatter + pattern, end="")
            print(spacePatter + pattern)
