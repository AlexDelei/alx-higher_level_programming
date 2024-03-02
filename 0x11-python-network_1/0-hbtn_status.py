#!/usr/bin/python3
"""
Fetching from https://alx-intranet.hbtn.io/status
"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    with urllib.request.urlopen(url) as resp:
        content = resp.read()
        utf_cont = content.decode('utf-8')

        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {utf_cont}")
