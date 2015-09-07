# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type s: str
    # :type t: str
    # :rtype: int
    def numDistinct(self, s, t):
        f = [[0 for col in range(len(s) + 1)] for row in range(len(t) + 1)]
        for col in range(len(s) + 1):
            f[0][col] = 1
        for row in range(1, len(t) + 1):
            f[row][0] = 0
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] != s[j - 1]:
                    f[i][j] = f[i][j - 1]
                else:
                    f[i][j] = f[i][j - 1] + f[i - 1][j - 1]
        return f[len(t)][len(s)]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numDistinct("rabbbit", "rabit"))