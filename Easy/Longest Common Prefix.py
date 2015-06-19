# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs or "" in strs:
            return ""
        p = 0
        while True:
            t = strs[0][p]
            for s in strs:
                if s[p] != t:
                    return s[0:p]
                if p + 1 >= len(s):
                    return s[0:p+1]
            p += 1

if __name__ == '__main__':
    sol = Solution()
    #strs = ['aaa', 'aaab', 'ab']
    strs = ["a", "b"]
    print(sol.longestCommonPrefix(strs))
