# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[m][n]表示以[m][n]为右下的最大正方形的边长 注意是边长不是面积
初态：
第一行 f[0][j] = matrix[0][j], 0 <= j < n
第一列 f[i][0] = matrix[i][0], 0 <= i < m
终态：
max{f[m][n]}的平方
递推公式：
如果matrix[i][j]为0 f[i][j] = 0
如果matrix[i][j]为1 f[i][j] = min{f[i-1][j], f[i][j-1], f[i-1][j-1]} + 1
'''

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        f = [[0 for cor in range(n)] for row in range(m)]
        # 初始化
        for i in range(m):
            f[i][0] = int(matrix[i][0])
        for j in range(n):
            f[0][j] = int(matrix[0][j])
        # 递推
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
        # 终态
        return max([max(res) for res in f]) ** 2

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximalSquare(["00", "00"]))
    print(sol.maximalSquare([[1,1,1], [1,1,1], [1,1,1]]))