#!/usr/bin/python3
"""
a Python script that fetches
https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        con = response.read()
        print('Body response:')
        print(f"\t- type: {type(con)}")
        print(f"\t- content: {con}")
        print("\t- utf8 content: " + con.decode("utf-8"))
