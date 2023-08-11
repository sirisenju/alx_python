# !/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        squared_matrix = []
        for row in matrix:
            squared_matrix.append(list(map(lambda x: x * x, row)))
        return squared_matrix
    

if __name__ == "__main__":
    square_matrix_simple()