#!/usr/bin/python3
"""
prints a square with size
"""


def print_square(size):
    """prints a square of # with size 

    Args:
        size : length of square

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for k in range(size):
            print("#", end="")
        print()
