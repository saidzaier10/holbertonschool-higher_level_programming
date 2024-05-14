#!/usr/bin/python3


# Define a function named print_matrix_integer that takes a matrix as input
def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over each element in the row
        for i in range(len(row)):
            # Check if the current element is not the last element in the row
            if i != len(row) - 1:
                # Print the current element with a space after it
                print("{:d} ".format(row[i]), end="")
            else:
                # Print the last element without a space after it
                print("{:d}".format(row[i]), end="")
        print()
