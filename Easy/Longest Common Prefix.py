# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs or "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        p = 0
        while True:
            t = strs[0][p]
            for s in range(1, len(strs)):
                if strs[s][p] != t:
                    return strs[s][0:p]
                if p + 1 >= len(strs[s]):
                    return strs[s][0:p+1]
            p += 1

if __name__ == '__main__':
    sol = Solution()
    #strs = ['aaa', 'aaab', 'ab']
    strs = ["a", "ac"]
    print(sol.longestCommonPrefix(strs))
