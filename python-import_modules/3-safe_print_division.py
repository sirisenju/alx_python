# !/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        print("Inside result: {}".format(result))

    return result

a = 9
b = 3


if __name__ == "__main__":
   safe_print_division(a, b)