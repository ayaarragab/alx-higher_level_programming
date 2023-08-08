#!/usr/bin/python3
def uppercase(str):
    i = 1
    for c in str:
        if i == len(str):
            print('{}'.format(chr(ord(c) - 32)))
            break
        elif ord(c) in range(97, 123):
            print('{}'.format(chr(ord(c) - 32)), end="")
            i += 1
            continue
        print(c, end="")
        i += 1
