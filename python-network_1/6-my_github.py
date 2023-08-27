#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]

    # payload = {'username': username, 'password': pwd}
    res = requests.get(url, auth=(username, password))
    if res.status_code == 200:
        data = res.json()
        print(data['id'])
    else:
        print("None")
