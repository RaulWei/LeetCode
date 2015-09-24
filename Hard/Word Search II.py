# -*- coding: UTF-8 -*-
__author__ = 'wang'

import collections

'''
终于A了 简直要哭了 这题A的特别艰难 一直TLE
引入Trie后 我在findWords中构造出str 然后去判断它是否startsWith 是否可以从Trie中search
这样还是太慢了

更快的做法是维持一个node（Trie中的节点）
board走一步 node往下一层 同时做相应处理 这样是更快的 可以AC
最后的AC的代码中其实Trie中的search和startsWith是没有用到的
'''

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
                self.dfsFindWords(board, i, j, walked, "", trie.root, ret)
        return ret

    def dfsFindWords(self, board, x, y, walked, str, node, ret):
        if node.isWord:
            ret.append(str)
            node.isWord = False     # 去重
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return
        if walked[x][y] == 1:
            return
        if not board[x][y] in node.son:
            return
        node = node.son[board[x][y]]
        str += board[x][y]
        walked[x][y] = 1
        dirc = [[0, 1], [1, 0], [0, -1], [-1, 0]]   # 右 下 左 上
        for go in dirc:
            new_x, new_y = x + go[0], y + go[1]
            self.dfsFindWords(board, new_x, new_y, walked, str, node, ret)
        walked[x][y] = 0


if __name__ == '__main__':
    sol = Solution()
    board = [
      ['o', 'a', 'a', 'n'],
      ['e', 't', 'a', 'e'],
      ['i', 'h', 'k', 'r'],
      ['i', 'f', 'l', 'v']
    ]
    words = ["oath","pea","eat","rain"]
    print(sol.findWords(board, words))

    board_new = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
    words_new = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
    print(sol.findWords(board_new, words_new))

    board_fuck = ["a"]
    words_fuck = []
    print(sol.findWords(board_fuck, words_fuck))