#!/usr/bin/python3

for i in range(10):
    for x in range(10):
        print('{}{}'.format(i, x), end="")
        if x == 9 and i == 9:
            continue
        print(', ', end="")
print()
