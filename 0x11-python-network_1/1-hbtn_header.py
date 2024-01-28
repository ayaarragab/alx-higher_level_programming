#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found
in the header of the response.
"""


if __name__ == '__main__':
    from urllib import request
    from sys import argv

    request_a = request.Request(argv[1])
    with request.urlopen(request_a) as response:
        print(response.headers['X-Request-Id'])
