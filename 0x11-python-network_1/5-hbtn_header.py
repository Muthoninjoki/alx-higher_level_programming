#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the variable"""
import request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = request.get(url)
    print(r.headers.get("X-Request-Id"))
