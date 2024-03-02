#!/usr/bin/python3
"""
Takes in an email and sends a POST request to the passed URL
"""
import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': f"{sys.argv[2]}"}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as resp:
        page = resp.read().decode('utf-8')

        print(f"Your email is: {page}")
