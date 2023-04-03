#       COLUMNS
# ROWS -|----------->
#       |
import random


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.data = [[random.randint(0, 9) for j in range(columns)] for i in range(rows)]

    def __mul__(self, other):
        # colsA == rowsB
        if self.columns != other.rows:
            return "multiplying error!"

        # matrix[rowsA][colsB]
        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                result.data[i][j] = sum(self.data[i][kk] * other.data[kk][j] for kk in range(self.columns))

        return result

    # data[rows][columns]
    def __str__(self):
        result = ""
        for i in range(self.rows):
            result += self.data[i].__str__() + "\n"

        return result


if __name__ == '__main__':
    # rows, columns
    a = Matrix(2, 3)
    b = Matrix(3, 4)

    a.data = [[1, 1, 0],
              [1, 0, 2]]

    b.data = [[1, 0, 2, 1],
              [2, 1, 2, 0],
              [1, 1, 0, 3]]

    print(a)
    print(b)

    print(a * b)
