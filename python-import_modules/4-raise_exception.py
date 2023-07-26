# !/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("This is a type exception.")
    except TypeError as e:
        print("Exception:", e)


if __name__ == "__main__":
    raise_exception()