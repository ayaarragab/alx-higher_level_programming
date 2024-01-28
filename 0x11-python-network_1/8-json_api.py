#!/usr/bin/python3
"""
Write a Python script that takes in a
letter and sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    char = "" if len(argv) == 1 else argv[1]
    params = {"q": char}
    resp = requests.post('http://0.0.0.0:5000/search_user', data=params)

    try:
        json_data = resp.json()
        if json_data and json_data != {}:
            print(f'[{json_data["id"]}] {json_data["name"]}')
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')
