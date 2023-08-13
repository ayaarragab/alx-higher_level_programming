#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1 and len(tuple_b) == 1:
        result = (tuple_b[0] + tuple_a[0], 0)
        return result
    elif len(tuple_a) == 1 and len(tuple_b) > 1:
        result = (tuple_b[0] + tuple_a[0], tuple_b[1])
        return result
    elif len(tuple_a) > 1 and len(tuple_b) == 1:
        result = (tuple_b[0] + tuple_a[0], tuple_a[1])
        return result
    elif len(tuple_a) > 1 and len(tuple_b) > 1:
        result = (tuple_b[0] + tuple_a[0], tuple_a[1] + tuple_b[1])
        return result
    elif len(tuple_a) == 0 and len(tuple_b) > 1:
        result = (tuple_b[0], tuple_b[1])
        return result
    elif len(tuple_b) == 0 and len(tuple_a) > 1:
        result = (tuple_a[0], tuple_a[1])
        return result
    elif len(tuple_b) == 0 and len(tuple_a) == 0:
        result = (0, 0)
        return result
