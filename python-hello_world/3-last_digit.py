#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_num = number - (10 * int(number / 10))
if new_num > 5:
    print("Last digit of", number, "is", new_num, "and is greater than 5")
elif new_num < 6:
    print("Last digit of", number, "is", new_num, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", new_num, "and is 0")
