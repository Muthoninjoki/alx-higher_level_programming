#!/usr/bin/python3
"""Defines a square"""


class Square:
    """definition"""
    def __init__(self, size=0):
        """Initialization"""
        self.__size = size

    @property
    def size(self):
        """Retrieving the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
