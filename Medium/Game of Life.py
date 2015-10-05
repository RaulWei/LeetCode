# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type board: List[List[int]]
    # :rtype: void Do not return anything, modify board in-place instead.
    def gameOfLife(self, board):
        row, col = len(board), len(board[0])
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in range(row):
            for j in range(col):
                count = 0   # 统计board[i][j]周围的live个数
                for dire in direction:
                    new_i, new_j = i + dire[0], j + dire[1]
                    if 0 <= new_i < row and 0 <= new_j < col and board[new_i][new_j] & 1 == 1:
                        count += 1
                if board[i][j] & 1 == 1 and (count == 3 or count == 2):
                    board[i][j] |= 2
                if board[i][j] & 1 == 0 and count == 3:
                    board[i][j] |= 2
        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1