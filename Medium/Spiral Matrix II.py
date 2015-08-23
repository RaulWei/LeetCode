# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type n: int
    # :rtype: List[List[int]]
    def generateMatrix(self, n):
        matrix = [[0 for col in range(n)] for row in range(n)]
        step = 1
        i, j = 0, 0
        while step <= n * n:
            while j < n and matrix[i][j] == 0:
                matrix[i][j] = step
                step += 1
                j += 1
            j -= 1
            i += 1
            while i < n and matrix[i][j] == 0:
                matrix[i][j] = step
                step += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and matrix[i][j] == 0:
                matrix[i][j] = step
                step += 1
                j -= 1
            j += 1
            i -= 1
            while i >=0 and matrix[i][j] == 0:
                matrix[i][j] = step
                step += 1
                i -= 1
            i += 1
            j += 1
        return matrix

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(3))