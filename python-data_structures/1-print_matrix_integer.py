# !/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            return "{}".format(num, end="")
        print()


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])