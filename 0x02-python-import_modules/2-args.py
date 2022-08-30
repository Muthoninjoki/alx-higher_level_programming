#!/bin/usr/python3

import sys

if __name__ == "__main__":
    n = 1
    length = len(sys.argv) - 1

    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
    else:
        print("{:d} arguments:".format(length))
    while n <= length:
        print("{:d}: {:s}".format(n, sys.argv[n]))
        n += 1
