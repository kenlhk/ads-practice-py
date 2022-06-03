"""
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        # check if first elements of rows and columns have zero
        col0 = any(matrix[i][0] == 0 for i in range(m))
        row0 = any(matrix[0][j] == 0 for j in range(n))

        # loop through entire matrix, indicate zero in the first elements of rows and column if zero is found
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # populate zeros if the first elements of rows and columns are zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # populate zeros in the first row and column
        if col0:
            for i in range(m):
                matrix[i][0] = 0
        if row0:
            for j in range(n):
                matrix[0][j] = 0

        print(matrix)


solution = Solution()
solution.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
