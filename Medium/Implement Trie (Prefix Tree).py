# -*- coding: UTF-8 -*-
__author__ = 'weimw'

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
        for w in word:
            for son in root.son:
                if w == son.char:
                    root = son
                    if w == word[-1] and root.isWord is True:
                        return True
                    break
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        root = self.root
        for w in prefix:
            for son in root.son:
                if w == son.char:
                    root = son
                    if w == prefix[-1]:
                        return True
                    break
        return False

if __name__ == '__main__':
    trie = Trie()
    trie.insert('s')
    trie.insert('so')
    trie.insert('keyy')
    print(trie.search('key'))
    print(trie.startsWith('key'))
