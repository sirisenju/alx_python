# !/usr/bin/python3

def no_c(my_string):
    arr = [my_string]
    for i in arr:
        if i == "c" or i == "C":
            arr.pop(i)
            return "{}".format(arr)
    return my_string


if __name__ == "__main__":
    no_c() 