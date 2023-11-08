#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result = []

    # Iterate through each row in the matrix
    for row in matrix:
        # Create a new row for the result matrix
        new_row = []

        # Iterate through each element in the row and square the value
        for element in row:
            squared_value = element ** 2
            new_row.append(squared_value)

        # Append the new row to the result matrix
        result.append(new_row)

    return result
