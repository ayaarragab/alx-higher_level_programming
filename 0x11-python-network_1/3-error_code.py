#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

if __name__ == '__main__':
    from urllib import request, parse, error
    from sys import argv

    request_b = request.Request(argv[1])
    try:
        with request.urlopen(request_b) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
