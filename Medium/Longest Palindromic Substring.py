# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[i][j]表示字符串从i到j是否为回文
初态：f[i][i] = True, 0 <= i < lens(s), f[i][j] = True, i > j 不存在的我们也认为它是
终态：f[i][j] = True and j-i最大
递推公式：
if f[i+1][j-1] == True s[i] == s[j]
    f[i][j] = True
'''

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        lens = len(s)
        f = [[False for col in range(lens)] for row in range(lens)]
        for i in range(lens):
            for j in range(lens):
                if i >= j:
                    f[i][j] = True
        for i in range(lens):
            for j in range(lens):
                if i+1 < lens and j-1 >= 0 and f[i+1][j-1] is True and s[i] == s[j]:
                    f[i][j] = True
        max, low, high = 0, 0, 0
        for i in range(lens):
            for j in range(lens):
                if f[i][j] is True:
                    if max < j - i:
                        max = j - i
                        low = i
                        high = j
        return s[low: high+1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('34543'))
    print(sol.longestPalindrome('bb'))
