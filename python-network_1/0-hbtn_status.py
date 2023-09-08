#!/usr/bin/python3
"""script that fetches 'https://alx-intranet.hbtn.io/status' """
import requests

url = "https://intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    data_type = type(response.text).__name__
    content = response.text
    content_length = len(content)
    
    print("Body response:")
    print(f"\t- type: {data_type}")
    print(f"\t- content: {content}")
    print(f"({content_length} chars long)")
else:
    print(f"Error: Unable to fetch the URL. Status code: {response.status_code}")
