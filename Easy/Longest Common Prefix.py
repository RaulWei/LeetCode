# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
模拟题 找出一组字符串的最长公共前缀
'''

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
            if p < len(strs[0]):
                t = strs[0][p]
            else:
                return strs[0]
            for s in range(1, len(strs)):
                if p >= len(strs[s]):
                    return strs[s]
                if strs[s][p] != t:
                    return strs[s][0:p]
            p += 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(['aaa', 'aaab', 'ab']))
    print(sol.longestCommonPrefix(['a', 'ac']))
    print(sol.longestCommonPrefix(['a', 'b']))
