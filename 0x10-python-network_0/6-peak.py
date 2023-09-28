#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ max number process"""
    max_n = None
    for i in list_of_integers:
        if max_n is None or max_n < i:
            max_i = i
    return max_i
