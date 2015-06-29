# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for r in range(1, row):
            if matrix[r][0] == 0:
                for c in range(1, col):
                    matrix[r][c] = 0
        for c in range(1, col):
            if matrix[0][c] == 0:
                for r in range(1, row):
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
            for c in range(col):
                matrix[0][c] = 0
        pass

if __name__ == '__main__':
    sol = Solution()
