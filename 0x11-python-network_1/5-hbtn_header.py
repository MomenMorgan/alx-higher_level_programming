#!/usr/bin/python3
"""equest to the URL and displays the value of
   the variable X-Request-Id """

if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    res = requests.get(url)
    head = res.headers.get('X-Request-Id')
    print(head)
