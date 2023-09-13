#!/usr/bin/python3
"""
This module contains a function that inserts a
line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a
    line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r+", encoding='UTF-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            for c in line:
                if c == '\n':
                    if search_string in line:
                        file.write(new_string)
