# -*- coding: UTF-8 -*-
__author__ = 'wang'

class TrieNode:
    # Initialize your data structure here.
    def __init__(self, char=''):
        self.son = []
        self.isWord = False
        self.char = char

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        root = self.root
        for i in range(len(word)):
            find = False
            for son in root.son:
                if word[i] == son.char:
                    # 在root的son中找到word的某个字符
                    root = son
                    find = True
                    break
            if find is False:
                # w不存在于root的son中
                root.son.append(TrieNode(word[i]))
                root = root.son[-1]
            if i == len(word) - 1:
                root.isWord = True
        return

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        root = self.root
        for i in range(len(word)):
            find = False
            for son in root.son:
                if word[i] == son.char:
                    # 找到word[i]
                    root = son
                    find = True
                    if i == len(word) - 1 and root.isWord is True:
                        return True
                    break
            if find is False:
                # word[i]没找到 可以直接返回False
                return False
        # 例如insert('ab'), search('a')
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        root = self.root
        for i in range(len(prefix)):
            find = False
            for son in root.son:
                if prefix[i] == son.char:
                    root = son
                    find = True
                    if i == len(prefix) - 1:
                        return True
                    break
            if find is False:
                # prefix[i]没找到可以直接返回False
                return False

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
    trie = Trie()
    sol = Solution()
    print(sol.findWords(["oaan", "etae", "ihkr", "iflv"], ["eat", "oath"]))