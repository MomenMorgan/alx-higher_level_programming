#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    max_n = None
    for i in list_of_integers:
        if max_n is None or max_n < i:
            max_i = i
    return max_i
