# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[i][j]表示word1[i]变化到word2[j]的编辑距离
初态：
终态：f[len(word1) - 1][len(word2) - 1]
递推公式：

'''

class Solution(object):
    # :type word1: str
    # :type word2: str
    # :rtype: int
    def minDistance(self, word1, word2):
        f = [[0 for col in range(len(word2))] for row in range(len(word1))]
        # 初始化
        for i in range(len(word1)):
            f[i][0] = i
        for j in range(len(word2)):
            f[0][j] = j
        # 动态规划
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    pass
