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

    if not first_name or not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if last_name and not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    if first_name and last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
