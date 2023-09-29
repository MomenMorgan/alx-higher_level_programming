#!/usr/bin/python3
"""email, sends a POST request to the
passed URL with the email as a parameter"""


if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.parse import urlencode
    from sys import argv
    val = {"email": argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        res = response.read().decode("utf-8")
        print(res)
