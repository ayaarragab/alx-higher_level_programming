#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    url = 'https://api.github.com/user'
    autho = (argv[1], argv[2])
    response = requests.get(url, auth=autho)
    if response.status_code == 200:
        user_id = response.json().get('id')
        print(user_id)
    else:
        print(None)
