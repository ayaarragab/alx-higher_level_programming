#!/usr/bin/python3
"""This module contains a function hat returns
True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance
    from the specified class ; otherwise False
    """
    return (isinstance(obj, a_class) and not type(obj) is a_class)
