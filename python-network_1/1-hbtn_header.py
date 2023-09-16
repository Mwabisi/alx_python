#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the
   X-Request-Id variable found in the header of the response"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id', 'X-Request-Id header not found')
    print(request_id)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}") 