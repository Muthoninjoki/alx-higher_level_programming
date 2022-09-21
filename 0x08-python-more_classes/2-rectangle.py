#!/usr/bin/python3
"""this module contains a Rectangle class"""


class Rectangle:
    """ This defines a Rectangle.
    width and height which are not integers
    """
    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle instance

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """ This is a getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ This assigns value to width"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self, value):
        """ This assigns a new value to attribute height"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ This method returns the area of the rectangle"""
        if self.__height == 0 or self.__width == 0|:
            return 0
        else:
            return (self.__height + self.__width) * 2






