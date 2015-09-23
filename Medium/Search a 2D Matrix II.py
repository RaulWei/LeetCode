# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type matrix: List[List[int]]
    # :type target: int
    # :rtype: bool
    def searchMatrix(self, matrix, target):
        row_n, col_n = len(matrix), len(matrix[0])
        cur = [0, col_n - 1]
        while 0 <= cur[0] < row_n and 0 <= cur[1] < col_n:
            if target == matrix[cur[0]][cur[1]]:
                return True
            elif target > matrix[cur[0]][cur[1]]:
                cur[0] += 1
            else:
                cur[1] -= 1
        return False

if __name__ == '__main__':
    sol = Solution()
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    matrix_2 = [[1, 1]]
    matrix_3 = [
        [ 1, 2, 3, 4, 5],
        [ 6, 7, 8, 9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ]
    print(sol.searchMatrix(matrix_3, 15))
    print(sol.searchMatrix(matrix, 5))
    print(sol.searchMatrix(matrix, 20))
    print(sol.searchMatrix(matrix_2, 0))