#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    l_len = len(my_list) - 1

    while(l_len >= 0):
        print("{:d}".format(my_list[l_len]))
        l_len -= 1
