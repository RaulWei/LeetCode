# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type board: List[List[str]]
    # :type words: List[str]
    # :rtype: List[str]
    def findWords(self, board, words):
        ret = []
        for w in words:
            if self.exist(board, w):
                ret.append(w)
        return ret

    # :type board: List[List[str]]
    # :type word: str
    # :rtype: bool
    def exist(self, board, word):
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
                # 新点合法 且能匹配 且没走过
                walked[new_i][new_j] = 1
                if self.DFS(new_i, new_j, board, word, index + 1, walked):
                    return True
                walked[new_i][new_j] = 0    # 注意复原
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.findWords(["oaan", "etae", "ihkr", "iflv"], ["eat", "oath"]))