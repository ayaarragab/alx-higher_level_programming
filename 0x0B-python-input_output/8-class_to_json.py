#!/usr/bin/python3
"""
a function that returns the dictionary description
for specific object
"""

import json


def class_to_json(obj):
    """
    a function that returns the dictionary description
    for specific object
    """
    return obj.__dict__
