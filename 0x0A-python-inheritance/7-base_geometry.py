#!/usr/bin/python3
"""This module contains an empty class BaseGeometry."""


class BaseGeometry:
    """an empty class BaseGeometry."""
    def area(self):
        """area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator"""
        if not type(value) is int or not type(value) is float:
            raise TypeError(f'{name} must be an integer')
        value = int(value)
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
