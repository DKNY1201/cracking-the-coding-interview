"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.
"""
import unittest


def zero_matrix(matrix):
    if not matrix or len(matrix[0]) == 0:
        return matrix

    zero_row_indexes = set()
    zero_col_indexes = set()
    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_row_indexes.add(i)
                zero_col_indexes.add(j)

    for r in zero_row_indexes:
        for c in range(m):
            matrix[r][c] = 0

    for c in zero_col_indexes:
        for r in range(n):
            matrix[r][c] = 0


class Test(unittest.TestCase):
    def test_zero_matrix(self):
        matrix = [
            [1, 2, 0, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [13, 14, 0, 16, 17, 18],
            [19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 0, 30],
            [31, 32, 33, 34, 35, 36]
        ]
        expected = [
            [0, 0, 0, 0, 0, 0],
            [7, 8, 0, 10, 0, 12],
            [0, 0, 0, 0, 0, 0],
            [19, 20, 0, 22, 0, 24],
            [0, 0, 0, 0, 0, 0],
            [31, 32, 0, 34, 0, 36]
        ]
        zero_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct zero matrix")

        matrix = [
            [1, 2, 3, 4, 5],
            [6, 0, 0, 0, 0],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 0, 0, 0],
            [16, 0, 0, 0, 0],
            [21, 0, 0, 0, 0]
        ]
        zero_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct zero matrix")

        matrix = [
            [1, 2, 3, 0],
            [5, 6, 0, 8],
            [9, 0, 11, 12],
            [0, 14, 15, 16]
        ]
        expected = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        zero_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct rotated matrix")

        matrix = [
            [4, 5, 2],
            [8, 0, 11],
            [9, 15, 100]
        ]
        expected = [
            [4, 0, 2],
            [0, 0, 0],
            [9, 0, 100]
        ]
        zero_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct rotated matrix")

        matrix = []
        expected = []
        zero_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return empty matrix if input matrix is empty")
