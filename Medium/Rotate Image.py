# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        self.up_down_reverse(matrix)
        self.diagonal_reverse(matrix)

    def up_down_reverse(self, matrix):
        t, n = 0, len(matrix)
        for i in range(n / 2):
            for j in range(n):
                t = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][j]
                matrix[n-1-i][j] = t

    def diagonal_reverse(self, matrix):
        t, n = 0, len(matrix)
        for i in range(n):
            for j in range(i):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t