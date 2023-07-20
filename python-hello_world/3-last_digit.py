#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_num = abs(number) % 10
if abs(number) % 10 > 5:
    print("Last digit of", number, "is", -new_num, "and is greater than 5")
elif abs(number) % 10 < 6:
    print("Last digit of", number, "is", -new_num, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", -new_num, "and is 0")
