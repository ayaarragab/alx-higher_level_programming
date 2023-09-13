#!/usr/bin/python3
"""
This module contains a function that returns an object
(Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    a function that returns an object
    (Python data structure) represented by
    a JSON string
    """
    return json.loads(my_str)
