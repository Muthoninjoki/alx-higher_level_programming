#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for i in range(len(matrix[n])):
            print("{:d}".format(matrix[n][i]), end="")
            if i != (len(matrix[n]) - 1):
                print(" ", end="")
        print("")
