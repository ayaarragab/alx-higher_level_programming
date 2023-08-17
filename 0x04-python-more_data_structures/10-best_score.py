#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxi = 0
    for key, val in a_dictionary.items():
        maxi = key
        break
    for key, val in a_dictionary.items():
        maxi = key if key > maxi else maxi
    return maxi
