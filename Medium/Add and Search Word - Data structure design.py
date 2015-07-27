# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
添加和查找单词
字典树 + 回溯法
'''

class TrieNode:
    # 字典树节点的数据结构
    def __init__(self, char=''):
        self.son = []
        self.char = char
        self.isWord = False

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        root = self.root
        for i in range(len(word)):
            find = False
            for w in root.son:
                if w.char == word[i]:
                    root = w
                    find = True
                    break
            if find is False:
                root.son.append(TrieNode(word[i]))
                root = root.son[-1]
            if i == len(word) - 1:
                root.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchWord(word, self.root)

    def searchWord(self, word, rt):
        # 将word[0]与rt的son们匹配

        # 前两个if是结束条件
        if not rt:
            # word还没匹配完
            return False
        if not word:
            return rt.isWord

        # 分类讨论 '.'和非'.'
        if word[0] == '.':
            for son in rt.son:
                if self.searchWord(word[1::], son):
                    return True
            return False
        else:
            find = False
            for son in rt.son:
                if word[0] == son.char:
                    find = True
                    return self.searchWord(word[1::], son)
            return find

if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("a")
    wordDictionary.addWord("a")
    print(wordDictionary.search("."))
    print(wordDictionary.search("a"))
    print(wordDictionary.search("aa"))
    print(wordDictionary.search("a"))
    print(wordDictionary.search(".a"))
    print(wordDictionary.search("a."))
