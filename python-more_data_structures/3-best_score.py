# !/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    max_key = None
    max_value = float('-inf')  # Initialize to negative infinity
    
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_value:
            max_key = key
            max_value = value
    
    return max_key


if __name__ == "__main__":
    best_score()