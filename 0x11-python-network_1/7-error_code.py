#!/usr/bin/python3
"""
sending a get request to a URL and display the body of response
and the status code of the response page
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
