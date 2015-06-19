# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[m][n]为到达[m][n]的路径数 它只能从左邻的格子过来 或者 上邻的格子下来
初态： f[i][0] = 1, 0 <= i < m; f[0][j] = 1, 0 <= j < n
终态： f[m-1][n-1]
递推公式： f[i][j] = f[i-1][j] + f[i][j-1]
'''

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        f = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            f[i][0] = 1
        for j in range(n):
            f[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]
        pass

if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(3, 7))
