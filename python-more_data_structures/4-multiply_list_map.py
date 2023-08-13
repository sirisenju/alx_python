def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x: x * number, my_list))
    return new_list

if __name__ == "__main__":
    multiply_list_map()