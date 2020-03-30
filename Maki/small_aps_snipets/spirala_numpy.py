import numpy as np
from sys import stdout


def print_matrix_spiral(matrix):
    
    while True:
        for i in range(len(matrix[0])):
            print(matrix[0, i], end=", ")

        # exit the while loop once we printed the last remaining elements
        if len(matrix) == 1:
            break

        # remove the just printed elements
        matrix = matrix[1:, :]

        matrix = np.transpose(matrix)

        # flips the matrix upside down
        matrix = np.flipud(matrix)

    # remove the last ", " from the print statement
    stdout.write("\b\b")
    stdout.close()


if __name__ == '__main__':

    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 'a'],
              ['b', 'c', 'd', 'e', 'f'],
              ['g', 'h', 'i', 'j', 'k']]

    matrix = np.array(matrix)
    print_matrix_spiral(matrix)
