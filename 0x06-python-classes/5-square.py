#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    def __init(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            slef.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        """print square to stdout in # char"""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
