#!/usr/bin/python3
"""Defines square"""


class Square:
    """Represents a square
    private instance attribute size
    private instance attribute position
    optional size and optional position
    Public instance method: area
    Public instance method: my_print
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializing the data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieving the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieving the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the position to a value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
       """Returning the current squarearea"""
        return self.__size ** 2

    def my_print(self):
        """Printing to stdout
        at the position given by positive attribute
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print() 
