#!/usr/bin/python3
"""
Takes in one argument: a letter
jsonify's the argument
searches a user withe the letter and returns the id and name
"""
import requests
import sys


if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    try:
        r = requests.post(url, data={'q': q})
        if not r.json():
            print("No result")
        else:
            print("[{}] {}".format(
                                   r.json()['id'],
                                   r.json()['name']))
    except ValueError:
        print("Not a valid JSON")
