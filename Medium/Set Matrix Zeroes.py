# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
矩阵中遇到0 则把该0所在行和列都替换成0
要求空间复杂度为常数 并且Do it in place

我的思路是如果遇到0 则把该0所在行的第一个数变为0 所在列的第一个数变为0
这对后序遍历没有影响 因为该行和该列的第一个数都已经遍历过
如果要标记为0的数为矩阵左上角第一个 则特殊讨论

遍历完矩阵后 开始in place地更改矩阵
1 重新遍历矩阵的第一列 如果遇到为0 则把该行全变0
2 重新遍历矩阵的第一行 如果遇到为0 则把该列全变0
3 判断左上角第一个数的flag zeroRow和zeroCol 处理第一行和第一列
'''

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        zeroRow = False
        zeroCol = False
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    if r == 0 and c == 0:
                        zeroRow, zeroCol = True, True
                    elif r == 0:
                        zeroRow = True
                    elif c == 0:
                        zeroCol = True
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        # 遍历第一列 遇到0 则把该行全变0
        for r in range(1, row):
            if matrix[r][0] == 0:
                for c in range(1, col):
                    matrix[r][c] = 0
        # 遍历第一行 遇到0 则把该列全变0
        for c in range(1, col):
            if matrix[0][c] == 0:
                for r in range(1, row):
                    matrix[r][c] = 0
        # 特殊考虑左上角
        if zeroRow is True:
            for c in range(col):
                matrix[0][c] = 0
        if zeroCol is True:
            for r in range(row):
                matrix[r][0] = 0
        return

if __name__ == '__main__':
    sol = Solution()
