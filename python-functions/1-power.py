# !/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)
    else:
        return(pow(a, b))