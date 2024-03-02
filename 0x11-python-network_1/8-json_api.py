#!/usr/bin/python3
"""
Takes in one argument: a letter
jsonify's the argument
searches a user withe the letter and returns the id and name
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'user': q})
    if not r.json():
        print("No result")
    elif '{' and '}' and ':' not in r.json():
        print("Not a valid JSON")
    else:
        print(f"[{r.json()[id]}] {r.json[name]}")
