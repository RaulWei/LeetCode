# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
f[m][n]为到达[m][n]的最小路径花费 它只能从左邻的格子过来 或者 从上邻的格子下来
初态： f[0][j] = sum(grid[0][0~j]), f[i][0] = sum(grid[0~i][0])
终态： f[m-1][n-1]
递推公式： f[i][j] = min{f[i][j-1], f[i-1][j]} + grid[i][j]
'''

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        f = [[0 for col in range(n)] for row in range(m)]
        # 初始化
        sum = 0
        for i in range(m):
            sum += grid[i][0]
            f[i][0] = sum
        sum = 0
        for j in range(n):
            sum += grid[0][j]
            f[0][j] = sum
        # 递推
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = min(f[i][j-1], f[i-1][j]) + grid[i][j]
        # 终态
        return f[m-1][n-1]

if __name__ == '__main__':
    sol = Solution()
