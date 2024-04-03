#!/usr/bin/python3
"""
taking a url and an email and sending a POST request to the
URL and the passed email as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
