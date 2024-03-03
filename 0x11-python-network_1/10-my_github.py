#!/usr/bin/python3
"""
Taking my github credentials and using Github API to display
my id
"""
import requests
import sys


def github_user_data(usr, access_tkn):
    """
    Fetches the user's details from the url and token
    provided

    args:
    - access_tkn -> This is the user's fine graines token

    Return: jsonified data if the tkn is valid and page is found
    """
    url = f'https://api.github.com/users/{usr}'
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {access_tkn}",
            "X-GitHub-Api-Version": "2022-11-28"
            }
    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        return resp.json()
    else:
        return None


if __name__ == '__main__':
    username = sys.argv[1]
    tkn = sys.argv[2]
    user_data = github_user_data(username, tkn)

    if user_data:
        id = user_data.get("id")
        print(id)
    else:
        print("User Not Found")
