#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
 handdle HTTPError."""

from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
