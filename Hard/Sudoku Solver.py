# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    def solveSudoku(self, board):
        """
          :type board: List[List[str]]
          :rtype: void Do not return anything, modify board in-place instead.
          """
        pass

    # 判断在board[x][y]处放置的数是否合法
    def isValid(self, board, x, y):
        target = board[x][y]
        for j in range(9):
            if j != y and board[x][j] == target:
                return False
        for i in range(9):
            if i != x and board[i][y] == target:
                return False
        for i in range((x / 3) * 3, (x / 3) * 3 + 3):
            for j in range((y / 3) * 3, (y / 3) * 3 + 3):
                if i != x and j != y and board[i][j] == target:
                    return False
        return True
