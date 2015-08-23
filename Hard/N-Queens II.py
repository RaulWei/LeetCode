# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# :type n: int
# :rtype: int
class Solution(object):
    def totalNQueens(self, n):
        board = [['.' for col in range(n)] for row in range(n)]
        res = []
        self.DFS(n, 0, res, board)
        return len(res)

    def DFS(self, n, row, res, board):
        if row == n:
            # 得到一组解 转换格式输出
            res.append(1)
            return
        for j in range(n):
            # 对某一确定行 循环判断其每一列找合格位置
            board[row][j] = 'Q'
            if self.isValid(row, j, n, board):
                self.DFS(n, row + 1, res, board)
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
    print(sol.totalNQueens(4))