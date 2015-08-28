# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type board: List[List[str]]
    # :type word: str
    # :rtype: bool
    def exist(self, board, word):
        # for i in range(len(board)):
        #     if len(board) == 1:
        #         board[i] = list(board[i])
        #     else:
        #         board[i] = list(board[i][0])
        walked = [[0 for col in range(len(board[0]))] for row in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    walked[i][j] = 1
                    if self.DFS(i, j, board, word, 1, walked):
                        return True
                    walked[i][j] = 0
        return False

    def DFS(self, i, j, board, word, index, walked):
        if index == len(word):
            return True
        dirc = [[0, 1], [1, 0], [0, -1], [-1, 0]]   # 右 下 左 上
        for go in dirc:
            new_i, new_j = i + go[0], j + go[1]
            if 0 <= new_i < len(board) and 0 <= new_j < len(board[new_i]) and board[new_i][new_j] == word[index] and walked[new_i][new_j] == 0:
                walked[new_i][new_j] = 1
                if self.DFS(new_i, new_j, board, word, index + 1, walked):
                    return True
                walked[new_i][new_j] = 0
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.exist(["ab", "cd"], "acdb"))
    print(sol.exist(["aa"], "aa"))
    print(sol.exist(["ABCE", "SFCS", "ADEE"], "ABCB"))
    print(sol.exist(["ABCE", "SFCS", "ADEE"], "ABCCED"))
    print(sol.exist(["ABCE", "SFCS", "ADEE"], "SEE"))
