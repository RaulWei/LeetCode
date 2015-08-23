# -*- coding: UTF-8 -*-
__author__ = 'weimw'
import copy
# :type n: int
# :rtype: List[List[str]]
class Solution(object):
    def solveNQueens(self, n):
        board = [['.' for col in range(n)] for row in range(n)]
        res = []
        self.DFS(n, 0, 0, res, board)
        return res

    def DFS(self, n, row, col, res, board):
        if row == n:
            tmp, r = copy.deepcopy(board), []
            for t in tmp:
                r.append(''.join(t))
            res.append(r)
            return
        for j in range(col, n):
            board[row][j] = 'Q'
            if self.isValid(row, j, n, board):
                self.DFS(n, row + 1, 0, res, board)
            board[row][j] = '.'

    def isValid(self, x, y, n, board):
        # 检查列
        for i in range(x):
            if board[i][y] == 'Q':
                return False
        # 检查行
        for j in range(y):
            if board[x][j] == 'Q':
                return False
        # 检查左斜向上
        i, j = x - 1, y - 1
        while i >=0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 检查右斜向上
        i, j = x - 1, y + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    sol.solveNQueens(4)