#!/usr/bin/python3
"""
Sending a request to the URL and display value of id found in the header
"""
import sys
import urllib.request

url = sys.argv[1]

if __name__ == '__main__':
    with urllib.request.urlopen(url) as resp:
        headers = resp.headers
        print(headers['X-Request-Id'])
