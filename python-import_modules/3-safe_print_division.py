# !/usr/bin/python3

def safe_print_division(a, b):
   try:
     result = a / b
   except ZeroDivisionError:
      print("Inside result: {}".format(None))
      print("{} / {} = {}".format(a, b, None))
   finally:
      return "Inside result: {}".format(a)
   

a = 9
b = 3


if __name__ == "__main__":
   safe_print_division(a, b)