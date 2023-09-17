#!/usr/bin/python3
"""
Square class module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    """Square inherits all attributes and methods of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)
    def area(self):
        return super().area()
    
    @property
    def size(self):
        """Size getter
        """
        return self._size

    @size.setter
    def size(self, value):
        """Size setter
        """

        # width not __width,
        # because you're calling width setter to set it to value

        self._size = value


sq = Square(3, 5, 4, 100)
print(sq)
print(sq.dth)
print(sq.area())
