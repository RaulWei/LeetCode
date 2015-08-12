# -*- coding: UTF-8 -*-
__author__ = 'weimw'

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
            while j < n and matrix[i][j] != '#':
                res.append(matrix[i][j])
                matrix[i][j] = '#'
                j += 1
            j -= 1
            i += 1
            while i < m and matrix[i][j] != '#':
                res.append(matrix[i][j])
                matrix[i][j] = '#'
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and matrix[i][j] != '#':
                res.append(matrix[i][j])
                matrix[i][j] = '#'
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and matrix[i][j] != '#':
                res.append(matrix[i][j])
                matrix[i][j] = '#'
                i -= 1
            i += 1
            j += 1
        return res
