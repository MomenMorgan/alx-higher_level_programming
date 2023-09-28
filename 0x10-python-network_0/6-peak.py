#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ max number process"""
    start = 0
    end = len(list_of_integers) - 1

    if list_of_integers == []:
        return None
    while start < end:
        mid = start + (end - start) // 2
        if list_of_integers[mid] > \
            list_of_integers[mid - 1]\
                and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start]
