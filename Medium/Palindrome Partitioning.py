# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
基本的回溯法 先切分后判断 循环加递归
'''

import copy

class Solution(object):
    # :type s: str
    # :rtype: List[List[str]]
    def partition(self, s):
        self.ret = []
        res = []
        self.DFS(s, res, 0)
        return self.ret

    def DFS(self, s, res, start):
        if start == len(s):
            self.ret.append(copy.deepcopy(res))
            return
        for i in range(start + 1, len(s) + 1):
            if self.isPalindrome(s[start:i]):
                res.append(s[start:i])
                self.DFS(s, res, i)
                res.pop()

    def isPalindrome(self, s):
        if not s:
            return False
        lens = len(s)
        for i in range(lens / 2):
            if s[i] != s[lens - i - 1]:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(""))
    print(sol.isPalindrome("1"))
    print(sol.isPalindrome("111"))
    print(sol.isPalindrome("dfd"))
    sol.partition("a")
    sol.partition("aab")
    sol.partition("cbbbcc")