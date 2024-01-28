#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable
X-Request-Id in the response header
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    params = {
        'email': argv[2]
    }
    res = requests.post(argv[1], data=params)
    print(res.text)
