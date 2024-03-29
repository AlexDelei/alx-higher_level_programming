#!/usr/bin/python3
"""
Fetching number of commits given the repo name and the username
"""
import sys
import requests


def get_commits(user, repo):
    """
    A function to fetch commits done on a certain repo

    args:
    - user -> This is the github username
    - repo -> repo to fetch from
    - tokn -> personal access token

    Return: a dictionary of the commits done on that repoo
    """
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    headers = {
            "Accept": "application/vnd.github+json",
            "X-Github-Api-Version": "2022-11-28"
            }
    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        return resp.json()
    else:
        return None


if __name__ == '__main__':
    repo = sys.argv[1]
    usr = sys.argv[2]

    user_data = get_commits(usr, repo)
    if user_data:
        for i, comm in enumerate(user_data[:10]):
            sha = comm['sha']
            name = comm['commit']['author']['name']
            print(f"{sha}: {name}", end="\n")
    else:
        print(None)
