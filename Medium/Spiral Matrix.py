# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
纯模拟走地图
右 - 下 - 左 - 上
'''

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0
        while len(res) < m * n:
            # 向右
            while j < n and matrix[i][j] != '#':
                res.append(matrix[i][j])
                matrix[i][j] = '#'
                j += 1
            j -= 1
            i += 1
            # 向下
            while i < m and matrix[i][j] != '#':
                res.append(matrix[i][j])
                matrix[i][j] = '#'
                i += 1
            i -= 1
            j -= 1
            # 向左
            while j >= 0 and matrix[i][j] != '#':
                res.append(matrix[i][j])
                matrix[i][j] = '#'
                j -= 1
            j += 1
            i -= 1
            # 向上
            while i >= 0 and matrix[i][j] != '#':
                res.append(matrix[i][j])
                matrix[i][j] = '#'
                i -= 1
            i += 1
            j += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(matrix))