#!/usr/bin/python3
"""sends a request to the URL and displays
the value of the X-Request-Id variable"""


if __name__ == "__main__":
    import urllib.request
    import sys
    from sys import argv
    with urllib.request.urlopen(sys.argv[1]) as response:
        Req = response.headers.get("X-Request-Id")
        print(Req)
