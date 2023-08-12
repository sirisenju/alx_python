# !/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary = {str(key): value}
    update_dictionary.update(a_dictionary)
    return update_dictionary