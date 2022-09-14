#!/usr/bin/python3
"""class Square that defines a square"""


class Square():
    """square class its proper validation and size"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size should be an int")
        elif (size < 0):
            raise ValueError("size should be >= 0")
        self.__size = size
