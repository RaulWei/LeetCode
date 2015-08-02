# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        dic = {}
        for w in s:
            if w in dic:
                dic[w] += 1
            else:
                dic[w] = 1

        for w in t:
            if w in dic:
                dic[w] -= 1
            else:
                return False

        for w in dic:
            if dic[w] != 0:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram('anagram', 'nagaram'))
