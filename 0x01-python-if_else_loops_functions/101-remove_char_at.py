#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    for count, c in enumerate(str):
        if count != n:
            str_copy += c
    return (str_copy)
