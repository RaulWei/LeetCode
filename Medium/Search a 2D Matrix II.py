# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type matrix: List[List[int]]
    # :type target: int
    # :rtype: bool
    def searchMatrix(self, matrix, target):
        row_n, col_n = len(matrix), len(matrix[0])
        return self.DFS(matrix, [0, 0], [row_n - 1, col_n - 1], target)

    def DFS(self, matrix, start, end, target):
        if start[0] < 0 or start[1] < 0 or end[0] < 0 or end[1] < 0:
            return False
        if start[0] >= len(matrix) or start[1] >= len(matrix[0]) or end[0] >= len(matrix) or end[1] >= len(matrix[0]):
            return False
        if start == end:
            return True if target == matrix[start[0]][start[1]] else False
        # if start[0] + 1 == end[0] and start[1] + 1 == end[1]:
        #     direction = [[0, 0], [0, 1], [1, 0], [1, 1]]
        #     for die in direction:
        #         if target == matrix[start[0] + die[0]][start[1] + die[1]]:
        #             return True
        #     return False
        med = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]
        if target == matrix[med[0]][med[1]]:
            return True
        elif target > matrix[med[0]][med[1]]:
            return self.DFS(matrix, [med[0] + 1, med[1] + 1], end, target) or self.DFS(matrix, [start[0], med[1] + 1], [med[0], end[1]], target) or self.DFS(matrix, [med[0] + 1, start[1]], [end[0], med[1]], target)
        else:
            return self.DFS(matrix, start, [med[0] - 1, med[1] - 1], target) or self.DFS(matrix, [start[0], med[1]], [med[0] - 1, end[1]], target) or self.DFS(matrix, [med[0], start[1]], [end[0], med[1] - 1], target)

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
    # print(sol.searchMatrix(matrix, 5))
    # print(sol.searchMatrix(matrix, 20))
    # print(sol.searchMatrix(matrix_2, 0))