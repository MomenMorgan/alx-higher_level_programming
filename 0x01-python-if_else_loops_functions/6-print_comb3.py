#!/usr/bin/python3

x = 0
while(x != 10):
    for number in range(x + 1, 10):
        if x == 8 and number == 9:
            print("{}{}".format(x, number))
        else:
            print("{}{}".format(x, number), end=", ")
    x = x + 1
