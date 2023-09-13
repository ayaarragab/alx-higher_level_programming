#!/usr/bin/python3
"""
This module contains a function that writes
a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    a function that writes
    a string to a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, "w", encoding="UTF-8") as f:
        count = 0
        for line in text:
            count += 1
            f.write(line)
        return (count)
