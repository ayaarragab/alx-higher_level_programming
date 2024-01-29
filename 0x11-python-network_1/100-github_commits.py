#!/usr/bin/python3
"""
`Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)`
=========================================================
Write a Python script that takes 2 arguments in order to
solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    try:
        for i in range(10):
            response = requests.get(url)
            if response.status_code == 200:
                sha = response.json()[i].get('sha')
                commit = response.json()[i].get('commit')
                autherName = commit.get('author').get('name')
                print(f'{sha}: {autherName}')
    except IndexError:
        pass
