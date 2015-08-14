# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        length = len(board)

        # row
        for i in range(length):
            valid = [0] * 10
            for j in range(length):
                if not self.isValidNum(valid, board[i][j]):
                    return False
        # col
        for j in range(length):
            for i in range(length):

        # subbox

    def isValidNum(self, valid, num):
        if num == '.' or (1 <= int(num) <= 9 and not int(num) in valid):
            valid[int(num)] = 1
            return True
        return False