#!/usr/bin/python3
"""
Taking my github credentials and using Github API to display
my id
"""
import requests
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    pwd = sys.argv[2]
    url = f'https://github.com/'
    r = requests.get(url, auth=(user, pwd))
    print(r.json()['id'])
