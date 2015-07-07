# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
f(i)表示以i结尾的包括i的能够形成word(True)或者不能形成word(False)
初态： f(0~n) = False
终态： 如果f(n) = True, n = len(s) - 1, 则表示s可以划分成几个word的拼接
递推公式： if f[k] == True and s[k+1: n] in dict: f[n] = True
'''

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return False
        f = [False for i in range(len(s))]
        for i in range(len(s)):
            for k in range(i + 1):
                if (k == 0 or f[k - 1] is True) and s[k: i + 1] in wordDict:
                    f[i] = True
        if f[len(s) - 1]:
            return True
        return False

if __name__ == '__main__':
    dict = ["leet", "code", "l"]
    sol = Solution()
    print(sol.wordBreak('leetcode', dict))

