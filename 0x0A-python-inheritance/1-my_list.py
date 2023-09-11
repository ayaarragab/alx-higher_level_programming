#!/usr/bin/python3
"""
This module includes a
class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def __init__(self):
        """init method that called once object is created"""
        super().__init__()

    def print_sorted(self):
        """
        print sorted list
        """
        newList = self.copy()
        newList.sort()
        print(newList)
