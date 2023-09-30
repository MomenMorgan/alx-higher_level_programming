#!/usr/bin/python3
"""equest to the URL and displays the value of
   the variable X-Request-Id """

if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(sys.argv[1])
    head = res.headers.get('X-Request-Id')
    print(head)
