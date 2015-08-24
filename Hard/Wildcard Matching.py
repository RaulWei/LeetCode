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
        # 特殊情况处理
        if not s:
            if not p:
                return True
            count = 0
            for i in range(len(p)):
                if p[i] != '*':
                    count += 1
            if count > 0:
                return False
            return True
        if not p:
            return False

        # 剪枝
        count_p = 0
        for c in range(len(p)):
            if p[c] != '*':
                count_p += 1
        if count_p > len(s):
            return False

        f = [[False for col in range(len(p) + 1)] for row in range(len(s) + 1)]

        f[0][0] = True
        for i in range(1, len(s) + 1):
            f[i][0] = False
        point = -1
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                point = j
                break
            f[0][j] = True
        if point != -1:
            for k in range(point, len(p) + 1):
                f[0][k] = False
        
        # 递推
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    f[i][j] = f[i-1][j-1]
                if p[j - 1] == '*':
                    f[i][j] = f[i][j-1] | f[i-1][j]

        # 返回终态
        return f[len(s)][len(p)]

if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch("aa", "a*"))
    print(sol.isMatch("c", "*?*"))