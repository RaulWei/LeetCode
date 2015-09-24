# -*- coding: UTF-8 -*-
__author__ = 'wang'
import collections

class TrieNode:
    # Initialize your data structure here.
    def __init__(self, char=''):
        self.son = collections.defaultdict(TrieNode)
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
            if word[i] not in root.son:
                root.son[word[i]] = TrieNode(word[i])
            root = root.son[word[i]]
        root.isWord = True
        return

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        root = self.root
        for i in range(len(word)):
            if word[i] not in root.son:
                # word[i]没找到 可以直接返回False
                return False
            root = root.son[word[i]]
        return root.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        root = self.root
        for i in range(len(prefix)):
            if prefix[i] not in root.son:
                return False
            root = root.son[prefix[i]]
        return True

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
            for j in range(len(board[0])):
                self.dfsFindWords(board, i, j, walked, "", trie, ret)
        return ret

    def dfsFindWords(self, board, x, y, walked, str, trie, ret):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return
        if walked[x][y] == 1:
            return
        str += board[x][y]
        if not trie.startsWith(str):
            return
        if trie.search(str) and str not in ret:
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

    board_new = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
    words_new = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
    print(sol.findWords(board_new, words_new))

    board_fuck = ["a"]
    words_fuck = []
    print(sol.findWords(board_fuck, words_fuck))