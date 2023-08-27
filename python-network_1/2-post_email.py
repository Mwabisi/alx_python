"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        url_page = response.read()
        decoded_html = url_page.decode('utf-8')
    print(decoded_html)
