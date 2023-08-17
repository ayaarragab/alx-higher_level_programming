#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    i = 0
    for key_origin, val in a_dictionary.items():
        if key_origin == key:
            a_dictionary[key_origin] = value
            i += 1
        else:
            continue
    if i == 0:
        a_dictionary[key] = value
    return a_dictionary
