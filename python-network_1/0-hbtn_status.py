import requests

url = "https://alu-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")