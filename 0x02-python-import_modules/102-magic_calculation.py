#!/usr/bin/python3
from magic_calculation_102 import *


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
    else:
        result = sub(a, b)
        return (result)
