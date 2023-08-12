# !/usr/bin/python3

def best_score(a_dictionary):
    for value in a_dictionary.values():
        if value == None:
            return "Best score: {}".format(None)
        
    max_values = max(a_dictionary.values())
    result = [key for key in a_dictionary if (a_dictionary[key] == max_values)]
    return "Best score: {}".format(result)


if __name__ == "__main__":
    best_score()