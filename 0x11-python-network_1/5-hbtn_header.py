#!/usr/bin/python3
"""
using requests module, takes a url, sends a request and
displays the value of the variable X-Request-id
"""
import sys
import requests


url = sys.argv[1]
r = requests.get(url)
print(r.headers['X-Request-Id'])
