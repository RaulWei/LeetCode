# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[i][j]表示从0-i的s与从0-j的p是否匹配
初态：f[0][j] f[i][0]
终态：f[len(s)-1][len(p)-1]
递推公式：
if s[i]==p[j] or p[j]=='?'
    f[i][j] = f[i-1][j-1]
if p[j]=='*'
    f[i][j] = f[i][j-1] or f[i-1][j-1] or f[i-2][j-1] or .. of f[0][j-1] = f[i][j-1] or f[i-1][j]
'''

# :type s: str
# :type p: str
# :rtype: bool
class Solution(object):
    def isMatch(self, s, p):
        if not s:
            if not p:
                return True
            for i in range(len(p)):
                if p[i] != '*':
                    return False
            return True
        if not p:
            return False

        count_p = 0
        for c in range(len(p)):
            if p[c] != '*':
                count_p += 1
        if count_p > len(s):
            return False

        f = [[False for col in range(len(p))] for row in range(len(s))]

        # 初始化初态f[0][j]
        if s[0] == p[0] or p[0] == '?' or p[0] == '*':
            f[0][0] = True
            point = 0
            for j in range(1, len(p)):
                if p[j] != '*':
                    point = j
                    break
                f[0][j] = True
            if point != 0:
                for k in range(point, len(p)):
                    f[0][k] = False
        else:
            for j in range(len(p)):
                f[0][j] = False
        # 初始化初态f[i][0]
        if p[0] == '*':
            for i in range(len(s)):
                f[i][0] = True
        else:
            for i in range(1, len(s)):
                f[i][0] = False

        # 递推
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if s[i] == p[j] or p[j] == '?':
                    f[i][j] = f[i-1][j-1]
                if p[j] == '*':
                    f[i][j] = f[i][j-1] | f[i-1][j]

        # 返回终态
        return f[len(s)-1][len(p)-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch("aa", "a*"))