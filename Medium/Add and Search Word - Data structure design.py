# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
添加和查找单词
字典树
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
                root.son.append(word[i])
                root = root.son[-1]
            if i == len(word) - 1:
                root.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):



# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
