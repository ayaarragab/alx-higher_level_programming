#!/usr/bin/python3
"""
a Python script that fetches
https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    from urllib import request


    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        print('Body response:')
        print(f"\t- type: {type(response.read())}")
        print(f"\t- content: {response.read()}")
        print("\t- utf8 content: " + response.read().decode("utf-8"))
