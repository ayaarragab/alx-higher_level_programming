#!/usr/bin/python3
"""
Task 4 doc
"""


def inherits_from(obj, a_class):
    """func doc"""
    return (isinstance(obj, a_class) and not type(obj) is a_class)
