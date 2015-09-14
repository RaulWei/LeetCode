# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
pal[i][j]表示s[i..j]是否为回文 f[i]表示把s[i...]切分为回文子串的最少切数
初态：pal[i][j] = False f[i] = n - 1 - i
终态：f[0]
递推公式：
if pal[i][j] == True:
    如果j == n - 1, f[i] = 0
    如果j != n - 1, f[i] = 1 + f[j + 1]
'''

class Solution(object):
    # :type s: str
    # :rtype: int
    def minCut(self, s):
        pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCut("sdfsfff"))