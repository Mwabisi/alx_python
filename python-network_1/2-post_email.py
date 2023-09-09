#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url, email = sys.argv[1], sys.argv[2]

try:
    response = requests.post(url, data={'email': email})
    if response.status_code == 200:
        print("Response body:")
        print(response.text)
    else:
        print(f"Error: HTTP status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")