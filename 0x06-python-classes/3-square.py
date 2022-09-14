#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """define"""
    def __init__(self, size=0):
        """initialize data"""
        if isinstance(size, int):
            self.__size = size
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
