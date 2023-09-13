#!/usr/bin/python3
"""
This is a sctipt that adds all
arguments to a Python list
then saves them to a file
"""

import sys
if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        myList = load(filename)
    except (FileNotFoundError):
        myList = []
        # in the previous solutions
        # you were making initialization by [] each time you run the program
    myList.extend(sys.argv[1:])
    save_to_json_file(myList, filename)
