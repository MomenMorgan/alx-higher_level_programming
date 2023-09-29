#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    res = requests.get(url).text

    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
