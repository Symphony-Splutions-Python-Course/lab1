from sys import stdout


def print_matrix_spiral(matrix, min_row, min_column, max_column, max_row):

    while min_row < max_row and min_column < max_column:

        # i stays the same | j++
        for j in range(min_column, max_column):
            print(matrix[min_row][j], end=', ')
        min_row += 1

        # i++ | j stays the same
        for i in range(min_row, max_row):
            print(matrix[i][max_column - 1], end=', ')
        max_column -= 1

        # i stays same | j--
        for j in range(max_column - 1, min_column - 1, -1):
            print(matrix[max_row - 1][j], end=', ')
        max_row -= 1

        # i-- | j stays the same
        for i in range(max_row - 1, min_row - 1, -1):
            print(matrix[i][min_column], end=', ')
        min_column += 1

    # remove the last ", " from the print statement
    stdout.write("\b\b")
    stdout.close()


if __name__ == '__main__':

    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 'a'],
              ['b', 'c', 'd', 'e', 'f'],
              ['g', 'h', 'i', 'j', 'k']]

    max_column = len(matrix[0])
    max_row = len(matrix)

    min_row = 0
    min_column = 0

    print_matrix_spiral(matrix, min_row, min_column, max_column, max_row)
