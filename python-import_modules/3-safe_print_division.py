# !/usr/bin/python3

def safe_print_division(a, b):
    try:
      result = a / b
    except ZeroDivisionError:
      print('Inside result: {}'.format("None"))
      print("{:d} / {:d} = {}".format(a, b, "None"))
    finally:
      print('Inside result: {}'.format(result))
      print("{:d} / {:d} = {}".format(a, b, result))

a = 9
b = 3


if __name__ == "__main__":
   safe_print_division(a, b)