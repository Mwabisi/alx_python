#!/usr/bin/python3
"""script that fetches 'https://alx-intranet.hbtn.io/status' """
import requests

url = "https://intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print("Body response:")
    print("\t- content:", content)
else:
    print(f"Error: Unable to fetch the URL. Status code: {response.status_code}")
