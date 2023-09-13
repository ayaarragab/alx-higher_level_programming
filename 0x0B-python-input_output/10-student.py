#!/usr/bin/python3
"""
This module contains class student
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """Initialization of the object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary
        representation of a Student instance
        """
        myDic = dict()
        allDic = self.__dict__
        if attrs:
            for item in attrs:
                for key in list(allDic.keys()):
                    if item is key:
                        myDic[key] = allDic.get(key)
                    else:
                        continue
            return (myDic)
        elif attrs == []:
            return myDic
        return (allDic)
