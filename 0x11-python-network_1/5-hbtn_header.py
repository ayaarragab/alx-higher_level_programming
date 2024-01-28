#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id in
the response header
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    res = requests.get(argv[1])
    if 'X-Request-Id' in res.headers.keys():
        print(res.headers['X-Request-Id'])
