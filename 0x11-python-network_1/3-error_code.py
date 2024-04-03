#!/usr/bin/python3
"""
sending a request to the url and display body of repsonse and handle error
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            page = resp.read().decode('utf-8')
            print(page)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
