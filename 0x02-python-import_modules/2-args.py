#!/usr/bin/python3

lenn = len(sys.argv) - 1

if lenn == 0:
    print("{:d} arguments.".format(lenn))
elif lenn == 1:
    print("{:d} argument:".format(lenn))
    print("{:d}: {}".format(lenn, sys.argv[1]))
else:
    i = 1
    print("{:d} arguments:".format(lenn))

    while(i <= lenn):
        print("{:d}: {}".format(i, sys.argv[i]))
        i += 1
