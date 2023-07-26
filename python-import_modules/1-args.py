# !/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    if len(argv) == 0:
        print("{} arguments.".format(0))
    elif len(argv) == 1:
        print("{} argument.".format(len(argv)))
        print("{}: {}".format(len(argv), argv[0]))
    else: 
        print("{} arguments.".format(len(argv)))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
    