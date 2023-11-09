#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    return [num*num for num in row[num] for row in matrix]  
