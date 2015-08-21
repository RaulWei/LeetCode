# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[i][j]表示从0-i的s与从0-j的p是否匹配
初态：f[0][j] f[i][0]
终态：f[len(s)-1][len(p)-1]
递推公式：
if s[i]==p[j] or p[j]=='?'
    f[i][j] = f[i-1][j-1] if s[i]==p[j] or p[j]=='?'
if p[j]=='*'
    f[i][j] = f[i][j-1] or f[i-1][j-1] or f[i-2][j-1] or .. of f[0][j-1] = f[i][j-1] or f[i-1][j]
'''

# :type s: str
# :type p: str
# :rtype: bool
class Solution(object):
    def isMatch(self, s, p):
        f = [[0] * len(p)] * len(s)

        # 初始化初态f[0][j]

        # 初始化初态f[i][0]
        if p[0] == '*':
            for i in range(len(s)):
                f[i][0] = True
        else:
            for i in range(1, len(s)):
                f[i][0] = False