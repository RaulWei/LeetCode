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
            if words[i] not in dic:
                dic[words[i]] = 1
            else:
                dic[words[i]] += 1
        for i in range(len(s) - word_len * word_num):
            if self.isivalid(i, s, word_num, word_len, dic):
                res.append(i)
        return res

    def isivalid(self, i, s, word_num, word_len, dic):
        k = 0
        while k < word_num:
            if s[i + word_len * k: i + word_len * (k + 1)] not in dic:
                return False
            dic[s[i + word_len * k: i + word_len * (k + 1)]] -= 1
            if dic[s[i + word_len * k: i + word_len * (k + 1)]] == 0:
                dic.pop(s[i + word_len * k: i + word_len * (k + 1)])
            k += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))