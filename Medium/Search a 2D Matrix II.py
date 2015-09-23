# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
给定的matrix的每行从左到右是升序的 每列从上到下是升序的
初始位置cur在第一行最后一列
如果target比cur大 那么第一行淘汰 cur下移一位
如果target比cur小 那么第一列淘汰 cur左移一位
如果target与cur相等 返回True
以此类推
'''

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
    print(sol.searchMatrix(matrix, 15))
    print(sol.searchMatrix(matrix, 5))
    print(sol.searchMatrix(matrix, 20))
    print(sol.searchMatrix(matrix, 0))