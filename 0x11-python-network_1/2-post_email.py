#!/usr/bin/python3
"""
a Python script that takes in a URL
and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
(decoded in utf-8)
"""

if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv

    values = {'email': argv[2]}
    query_string = parse.urlencode(values)
    query_string = query_string.encode("ascii")
    request_b = request.Request(argv[1], query_string)

    with request.urlopen(request_b) as response:
        content = response.read()
        print(content.decode("utf-8"))
