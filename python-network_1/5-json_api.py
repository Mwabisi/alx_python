#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""

    payload = {'q': q}
    res = urllib.request.post(url, data=payload)
    try:
        data = res.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
