#!/usr/bin/python3
"""
a Python script that fetches
https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(resp.text)}')
    print(f'\t- content: {resp.text}')
