"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
"""
import unittest


def rotate_matrix(matrix):
    """
    Swap layer by layer, from outside to inside. Observe the way i and j change to have a appropriate formula
    :param matrix:
    :return:
    """
    if not matrix:
        return

    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp


class Test(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35, 36]
        ]
        expected = [
            [31, 25, 19, 13, 7, 1],
            [32, 26, 20, 14, 8, 2],
            [33, 27, 21, 15, 9, 3],
            [34, 28, 22, 16, 10, 4],
            [35, 29, 23, 17, 11, 5],
            [36, 30, 24, 18, 12, 6]
        ]
        rotate_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct rotated matrix")

        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
        rotate_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct rotated matrix")

        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
        rotate_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct rotated matrix")

        matrix = [
            [4, 5, 2],
            [8, 9, 11],
            [9, 15, 100]
        ]
        expected = [
            [9, 8, 4],
            [15, 9, 5],
            [100, 11, 2]
        ]
        rotate_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct rotated matrix")

        matrix = [
            [1]
        ]
        expected = [
            [1]
        ]
        rotate_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return correct rotated matrix")

        matrix = []
        expected = []
        rotate_matrix(matrix)
        self.assertEqual(expected, matrix, "Should return empty matrix if input matrix is empty")
