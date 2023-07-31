# !/usr/bin/python3

def no_c(my_string):
    arr = [my_string]
    new_string = " "
    for i in arr:
        if i == "c" or i == "C":
            arr.pop(i)
            new_string.join(arr)
            return "{}".format(new_string)
    return "{}".format(my_string)

if __name__ == "__main__":
    no_c() 