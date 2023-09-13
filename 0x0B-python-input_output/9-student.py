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

    def to_json(self):
        """
        retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
