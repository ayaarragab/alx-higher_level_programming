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
        if x < 0:
            raise ValueError('x must be >= 0')
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
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """
        area
        """
        return self.__height * self.__width

    def display(self):
        """
        rectangle of #
        """
        pattern = ""
        for i in range(self.__x):
            pattern += " "
        pattern += '#' * self.__width
        for j in range(self.__y):
            print()
        for k in range(self.__height):
            print(pattern)

    def __str__(self):
        """
        str special method
        """
        strrr = (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                 f"{self.__width}/{self.__height}")
        return strrr

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding this method:
        that assigns an argument to each attribute

        args: arbitary positional arguments

        kwargs: arbitary keyword arguemts

        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation
        """
        mydict = dict()
        mydict["id"] = self.id
        mydict["x"] = self.x
        mydict["y"] = self.y
        mydict["width"] = self.width
        mydict["height"] = self.height
        return mydict
