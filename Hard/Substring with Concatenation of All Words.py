# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        res, dic = [], {}
        word_num, word_len = len(words), len(words[0])
        for i in range(word_num):
            dic[words[i]] = 1
        for i in range(len(s) - word_len):
            if self.isivalid(i, s, word_num, word_len, dic):
                res.append(i)
        return res

    def isivalid(self, i, s, word_num, word_len, dic):
        k = 0
        while k < word_num:
            if s[i + word_len * k: i + word_len * (k + 1)] not in dic:
                return False
            k += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))