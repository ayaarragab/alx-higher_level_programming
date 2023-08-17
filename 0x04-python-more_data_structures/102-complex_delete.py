#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_be_deleted = []
    if a_dictionary and value:
        for key, val in a_dictionary.items():
            if val == value:
                to_be_deleted.append(key)
            else:
                continue
        for key in to_be_deleted:
            del a_dictionary[key]
    return a_dictionary
