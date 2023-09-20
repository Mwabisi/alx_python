import requests
import sys

def get_x_request_id(url):
  """Gets the value of the X-Request-Id header from the response to the given URL.

  Args:
    url: The URL to send a request to.

  Returns:
    The value of the X-Request-Id header, or None if the header is not present in the response.
  """

  response = requests.get(url)
  x_request_id = response.headers.get("X-Request-Id")
  return x_request_id

if __name__ == "__main__":
  url = sys.argv[1]
  x_request_id = get_x_request_id(url)

  print(x_request_id)
