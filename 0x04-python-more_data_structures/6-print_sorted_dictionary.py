#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ListOfKeys = list(a_dictionary.keys())
    ListOfKeys = sorted(ListOfKeys)
    new_dic = dict()
    for key in ListOfKeys:
        for key2, val in a_dictionary.items():
            if a_dictionary[key] == a_dictionary[key2]:
                new_dic[key] = a_dictionary[key2]
    for key, value in new_dic.items():
        print(f'{key}: {value}')
