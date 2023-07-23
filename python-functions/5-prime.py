# !/usr/bin/python3
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True

    # Determine the maximum divisor to check
    max_divisor = int(number ** 0.5) + 1
    
    for divisor in range(2, max_divisor):
        if number % divisor == 0:
            return False

    return True