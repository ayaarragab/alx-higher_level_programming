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

    @property
    def size(self):
        """Size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter
        """

        # width not __width,
        # because you're calling width setter to set it to value

        self.width = value
        self.height = value

    def __str__(self):
        """Str magic method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def display(self):
        """
        Display
        """
        return super().display()

    def update(self, *args, **kwargs):
        """Update
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary
        """
        mydict = dict()
        mydict["id"] = self.id
        mydict["x"] = self.x
        mydict["y"] = self.y
        mydict["size"] = self.size
        return mydict
