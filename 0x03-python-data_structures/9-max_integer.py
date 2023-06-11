#!/usr/bin/python3
def max_integer(my_list=[]):

    llen = len(my_list)
    if llen == 0:
        return None
    else:
        max = my_list[0]
        for i in range(llen):
            if max < my_list[i]:
                max = my_list[i]
        return max
