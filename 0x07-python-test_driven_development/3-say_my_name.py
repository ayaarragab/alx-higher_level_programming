#!/usr/bin/python3
"""
This module contains a function that prints my name + "name"
say_my_name(first_name, last_name=""): func
return: my name is+ first_name + last_name
"""


def say_my_name(first_name, last_name=""):
    """param first_name: first name (str)
       param last_name:0 last_name (str)
       return: my name is+ first_name + last_name"""

    if first_name is None or not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if (last_name and not isinstance(last_name, str)) or (last_name is None):
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
