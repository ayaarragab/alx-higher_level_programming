#!/usr/bin/python3
"""
This module contains a function
that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="UTF-8") as f:
        text = f.readlines()
        for line in text:
            print(line, end="")
