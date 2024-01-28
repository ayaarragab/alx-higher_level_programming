#!/usr/bin/python3
"""
a Python script that fetches
https://alx-intranet.hbtn.io/status
"""


from urllib import request, parse


with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print('Body response:')
    print(f"    - type: {type(response.read())}")
    print(f"    - content: {response.read()}")
    print("    - utf8 content: " + response.read().decode("UTF-8"))
