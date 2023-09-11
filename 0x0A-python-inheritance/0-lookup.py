#!/usr/bin/python3
"""This module contains a function that
returns the list of available attributes and methods of an object"""


def lookup(obj):
    """
    returns the list of available attributes
    and methods of an object
    """
    return (list(dir(obj)))
