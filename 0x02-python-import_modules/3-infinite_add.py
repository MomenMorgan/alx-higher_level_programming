#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    lenn = len(argv) - 1
    res = 0

    if lenn > 0:
        for i in range(1, lenn + 1):

            res += int(argv[i])

    print("{:d}".format(res))
