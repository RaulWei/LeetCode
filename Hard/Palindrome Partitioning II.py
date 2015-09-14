# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
pal[i][j]表示s[i..j]是否为回文 f[i]表示把s[i...]切分为回文子串的最少切数
初态：pal[i][j] = False f[i] = n - 1 - i
终态：f[0]
递推公式：
if pal[i][j] == True:
    如果j == n - 1, f[i] = 0
    如果j != n - 1, f[i] = 1 + f[j + 1] (如果f[i] > 1 + f[j + 1]的情况下才更新)
'''

class Solution(object):
    # :type s: str
    # :rtype: int
    def minCut(self, s):
        lens = len(s)
        p = [[False for col in range(lens)] for row in range(lens)]
        f = [lens - 1 - i for i in range(lens)]
        for i in range(lens)[::-1]:
            for j in range(i, lens)[::-1]:
                if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1] is True):
                    p[i][j] = True
                    if j == lens - 1:
                        f[i] = 0
                    else:
                        f[i] = min(f[i], 1 + f[j + 1])
        return f[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.minCut("sdfsfff"))