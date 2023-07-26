# !/usr/bin/python3
from sys import argv

if len(argv) == 0:
    print("{} arguments.".format(len(argv)))
elif len(argv) == 1:
    print("{} arguments.".format(len(argv)))
    print("{}: {}".format(len(argv), argv[1]))
else: 
    print("{} arguments.".format(len(argv)))
    for i in range(1, len(argv)+1):
        print("{}: {}".format(i, argv[i]))
    