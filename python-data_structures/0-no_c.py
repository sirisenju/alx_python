# !/usr/bin/python3

def no_c(my_string):
    for i in my_string:
        if i == "c" or i == "C":
            my_string.pop(i)
            return my_string
    return my_string


if __name__ == "__main__":
    no_c() 