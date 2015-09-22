# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
f(x, y)表示从[x,y]到右下角所需的最少生命点数
'''

class Solution(object):
    # :type dungeon: List[List[int]]
    # :rtype: int
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 0
        row_n, col_n = len(dungeon), len(dungeon[0])
        f = [[0 for col in range(col_n)] for row in range(row_n)]
        for r in range(row_n)[::-1]:
            for c in range(col_n)[::-1]:
                if r == row_n - 1 and c == col_n - 1:
                    f[r][c] = max(0 - dungeon[r][c], 0)
                elif r == row_n - 1:
                    f[r][c] = max(f[r][c + 1] - dungeon[r][c], 0)
                elif c == col_n - 1:
                    f[r][c] = max(f[r + 1][c] - dungeon[r][c], 0)
                else:
                    f[r][c] = max(min(f[r + 1][c], f[r][c + 1]) - dungeon[r][c], 0)
        return f[0][0] + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculateMinimumHP([[0, 0]]))
    print(sol.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))