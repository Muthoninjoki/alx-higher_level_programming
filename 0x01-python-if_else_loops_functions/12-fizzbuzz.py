#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 15 == 0:
            print("{} ".format("FizzBuzz"), end='')
        elif n % 5 == 0:
            print("{} ".format("Buzz"), end='')
        elif n % 3 == 0:
            print("{} ".format("Fizz"), end='')
        else:
            print("{} ".format(n), end='')
