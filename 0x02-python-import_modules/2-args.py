#!/bin/usr/python3
if __name__ == "__main__":

    import sys
    position = len(sys.argv) - 1
    if position == 0:
        print("0 arguments.")

    elif position == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(count))

    for n in range(position):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
