#!/usr/bin/python3
"""
Sending a request to the URL and display value of id found in the header
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        headers = resp.headers
        print(headers['X-Request-Id'])
