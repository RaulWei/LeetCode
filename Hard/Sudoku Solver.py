# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
http://blog.csdn.net/sbitswc/article/details/20683945
这篇的思路很清晰 值得参考

先放置 再判断
如果合法则往下递归 如果不合法则清空刚才的放置进行下一次尝试

终态要return True 这个别忘了
'''

class Solution(object):
    def solveSudoku(self, board):
        """
          :type board: List[List[str]]
          :rtype: void Do not return anything, modify board in-place instead.
          """
        self.DFS(board)

    def DFS(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i][j] = k
                        if self.isValid(board, i, j) and self.DFS(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True

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
