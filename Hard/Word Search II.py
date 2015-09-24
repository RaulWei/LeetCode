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
        trie, ret = Trie(), []
        for w in words:
            trie.insert(w)
        walked = [[0 for col in range(len(board[0]))] for row in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.dfsFindWords(board, i, j, walked, "", trie, ret)
        return ret

    def dfsFindWords(self, board, x, y, walked, str, trie, ret):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return
        if walked[x][y]:
            return
        str += board[x][y]
        if not trie.startsWith(str):
            return
        if trie.search(str):
            ret.append(str)
        walked[x][y] = 1
        dirc = [[0, 1], [1, 0], [0, -1], [-1, 0]]   # 右 下 左 上
        for go in dirc:
            new_x, new_y = x + go[0], y + go[1]
            self.dfsFindWords(board, new_x, new_y, walked, str, trie, ret)
        walked[x][y] = 0


if __name__ == '__main__':
    sol = Solution()
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    print(sol.findWords(board, words))