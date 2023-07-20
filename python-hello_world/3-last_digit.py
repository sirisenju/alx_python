#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_num = number - (10 * int(number / 10))
if new_num > 5:
    print("the last digit of", number, "is", new_num, "and is greater than 5")
elif abs(number) % -10 < 6:
    print("the last digit of", number, "is", new_num, "and is less than 6 and not 0")
elif new_num == 0:
    print("the last digit of", number, "is", new_num, "and is 0")
