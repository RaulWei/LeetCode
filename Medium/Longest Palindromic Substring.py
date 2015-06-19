# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
求最长回文子串
'''

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s:
            return ""
        lens = len(s)
        longestPRes = s[0]
        i = lens / 2
        while i >= 0 and i < lens:
            step = 1
            longestP = s[i]
            while i - step >= 0 and i + step < lens:
                if s[i - step] == s[i + step]:
                    longestP = s[i - step] + longestP + s[i + step]
                else:
                    break
                step += 1
            if len(longestP) > len(longestPRes):
                longestPRes = longestP
                # 剪枝
                if len(longestPRes) >= (len(s) - i) * 2 or len(longestPRes) >= i * 2:
                    break
            i = (i + 1) * ((-1) ** (i % 2))
        return longestPRes

if __name__ == '__main__':
    sol = Solution()
    #print(sol.longestPalindrome('12345432'))
    print(sol.longestPalindrome('bb'))
