#!/usr/bin/python3
"""
This module contains a function
that appends a string at the end of a text file
(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    function
    that appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    with open(filename, "a", encoding="UTF-8") as f:
        count = 0
        for line in text:
            count += 1
            f.write(line)
        return (count)
