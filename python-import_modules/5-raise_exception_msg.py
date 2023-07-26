# !/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        raise NameError("C is fun")
    except NameError as e:
        print(e)

if __name__ == "__main__":
    raise_exception_msg()