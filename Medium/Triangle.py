# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[m][n]表示到达[m][n]的最短路径 它只能从上一个或者上左一个过来
初态：
初始化三角形的腰
f[0][0] = t[0][0], f[i][0] = f[i-1][0]+t[i][0], f[i][Ni] = f[i-1][Ni-1]+t[i][Ni], 1 <= i < m
终态：
min{f[m-1][j], 0 <= j < N(m-1)}
递推公式：
f[i][j] = min{f[i-1][j-1], f[i-1][j]} + t[i][j], 2 <= i < m, 1 <= j < Ni - 1
'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        m = len(triangle)
        f = [[0 for col in range(len(triangle[m-1]))] for row in range(m)]
        # 初始化
        f[0][0] = triangle[0][0]
        for i in range(1, m):
            f[i][0] = f[i-1][0] + triangle[i][0]
            ni = len(triangle[i]) - 1
            ni_1 = len(triangle[i-1]) - 1
            f[i][ni] = f[i-1][ni_1] + triangle[i][ni]
        # 遍历求dp数组
        for i in range(2, m):
            for j in range(1, len(triangle[i])-1):
                f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]
        return min(f[m-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
