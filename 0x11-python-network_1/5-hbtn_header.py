#!/usr/bin/python3
"""
using requests module, takes a url, sends a request and
displays the value of the variable X-Request-id
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    hed = r.headers
    print(hed['X-Request-Id'])
