#!/usr/bin/python3
""" This module contains a dummy adder func for testing"""


def add_integer(a, b=98):
    """ adds integers
        Args:
        @a: first integer
        @b: second integer, defaults to 98 if not given
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
