# !/usr/bin/python3

def no_c(my_string):
    lst = [i for i in my_string.lower() if i != "c"]
    newStr = "".join(lst)
    return newStr

if __name__ == "__main__":
    no_c() 