#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the
body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        response = requests.get(url)
        print("Response body:")
        print(response.text)

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except IndexError:
        print("Usage: python script.py <URL>")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}") 