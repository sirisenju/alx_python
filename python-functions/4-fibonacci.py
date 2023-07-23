# !/usr/bin/python3
def fibonacci_sequence(n):
    if n == 0:
        return []
    elif n == 1:
        return [0, 1]
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence