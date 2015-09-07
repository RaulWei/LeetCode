# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[i][j]表示t的前i个组成的子串变化到s的前j个组成的子串共有的变化种数
初态：f[0][col] = 1 (空t变化到s任何子串只有一种办法) f[row][0] = 0 (任何t的子串变化到空串都没办法 因为t到s只能是增加字符)
终态：f[len(t)][len(s)]
递推公式：
f[i][j] = f[i][j - 1] + (t[i - 1] != s[i - 1] ? 0:f[i - 1][j - 1])
'''

class Solution(object):
    # :type s: str
    # :type t: str
    # :rtype: int
    def numDistinct(self, s, t):
        f = [[0 for col in range(len(s) + 1)] for row in range(len(t) + 1)]
        # 初始化
        for col in range(len(s) + 1):
            f[0][col] = 1
        for row in range(1, len(t) + 1):
            f[row][0] = 0
        # 递推 分类讨论：t子串的最后一个字符与s子串的最后一个字符是否相同
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] != s[j - 1]:    # i和j分别表示t的前i个字符和s的前j个字符 对应下标要减一
                    f[i][j] = f[i][j - 1]
                else:
                    f[i][j] = f[i][j - 1] + f[i - 1][j - 1]
        return f[len(t)][len(s)]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numDistinct("rabbbit", "rabit"))