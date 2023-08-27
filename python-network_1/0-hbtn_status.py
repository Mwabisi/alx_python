#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    req = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        html = response.read()

    decoded_html = html.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {decoded_html}")