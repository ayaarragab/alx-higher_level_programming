#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxi = None
    for keyy, val in a_dictionary.items():
        maxi = val
        break
    for keyy, val in a_dictionary.items():
        maxi = val if val > maxi else maxi
    for key, vall in a_dictionary.items():
        if vall == maxi:
            return key
        else:
            continue
