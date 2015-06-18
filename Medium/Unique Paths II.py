# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[m][n]为到达[m][n]的路径数 它只能从左临的格子过来 或者 上临的格子下来
初态：
f[i][0] = 1, 0 <= i < m 如果发现obstacleGrid[i][0]为1 那么f[i][0]以及它下面全都为0
f[0][j] = 1, 0 <= j < n 如果发现obstacleGrid[0][j]为1 那么f[0][j]以及它右边全都为0
终态： f[m-1][n-1]
递推公式：
if obstacleGrid[i][j] == 1
    f[i][j] = 0
else f[i][j] = f[i-1][j] + f[i][j-1]
'''

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0 for col in range(n)] for row in range(m)]
        # 初始化
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for k in range(i, m):
                    f[k][0] = 0
                break
            else:
                f[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                for k in range(j, n):
                    f[0][k] = 0
                break
            else:
                f[0][j] = 1
        # 遍历求dp数组
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(sol.uniquePathsWithObstacles([[1, 0]]))
