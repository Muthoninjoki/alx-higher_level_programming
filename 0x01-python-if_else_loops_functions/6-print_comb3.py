#!/usr/bin/python3
for n in range(0, 9):
    for i in range(n + 1, 10):
        if n == 8 and i == 9:
            print("{:d}{}".format(n, i))
        print("{}{}".format(n, i), end=", ")
