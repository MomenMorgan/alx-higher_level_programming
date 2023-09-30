#!/usr/bin/python3
"""sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[2]

    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    send = requests.post(url, data=data)
    try:
        json = send.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
