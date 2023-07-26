# !/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("Exception has been raised")
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    raise_exception()