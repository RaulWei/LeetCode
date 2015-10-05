# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
根据规则更新一个board 但是不能用额外的空间
由于board上点的值不是0就是1 只用了1 bit
所以我们可以把update的值存在第二个bit
最后把所有结果右移1 bit消灭原始初值即可
'''

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
                    # 活着且有两个或者三个邻居活着 那么它可以继续活着
                    board[i][j] |= 2
                if board[i][j] & 1 == 0 and count == 3:
                    # 死了但是正好有三个邻居活着 那么它可以复活
                    board[i][j] |= 2
        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1