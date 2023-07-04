#!/usr/bin/python3
"""
prints "My name is" with the first and last name
"""


def say_my_name(first_name, last_name=""):
    """prints "My name is" with the first and last name

    Args:
        first_name : first name
        last_name : last name

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
    