#!/usr/bin/python3
"""
Takes in a URL, sends a request to that url and displays
the value of the X-request-id found in the response header
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
