# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type beginWord: str
    # :type endWord: str
    # :type wordDict: Set[str]
    # :rtype: int
    def ladderLength(self, beginWord, endWord, wordDict):
        pass

    def isOneChDiff(self, word1, word2):
        if len(word1) != len(word2):
            return False
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count == 1:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))