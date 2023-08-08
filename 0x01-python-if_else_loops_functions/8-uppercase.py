#!/usr/bin/python3
def uppercase(str):
    modified = ""
    for c in str:
        if ord(c) in range(97, 123):
            modified += chr(ord(c) - 32)
        else:
            modified += c
    print(modified.format(str))
