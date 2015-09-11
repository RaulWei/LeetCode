# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
1 从边界找到'O'
2 使用BFS把找到的'O'标记为'T'
3 遍历board 把'O'转换为'X' 把'T'转换为'O'
'''

class Solution(object):
    # :type board: List[List[str]]
    # :rtype: void Do not return anything, modify board in-place instead.
    def solve(self, board):
        row, col = len(board), len(board[0])
        # 边界：第一行 和 最后一行
        for j in range(col):
            if board[0][j] == 'O':
                self.bfsMark(board, 0, j)
            if board[row - 1][j] == 'O':
                self.bfsMark(board, row - 1, j)
        # 边界：最左列 和 最右列
        for i in range(row):
            if board[row][0] == 'O':
                self.bfsMark(board, row, 0)
            if board[row][col - 1] == 'O':
                self.bfsMark(board, row, col - 1)
        # 遍历board
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'

    def bfsMark(self, board, row, col):
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve(["XXXX", "XOOX", "XXOX", "XOXX"]))