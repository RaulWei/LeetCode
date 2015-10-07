# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type pattern: str
    # :type str: str
    # :rtype: bool
    def wordPattern(self, pattern, str):
        dic = dict()
        stri = str.split()
        if len(stri) != len(pattern):
            return False
        for i in range(len(stri)):
            if stri[i] in dic and dic[stri[i]] != pattern[i]:
                return False
            dic[str[i]] = pattern[i]
        return True

if  __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))
    print(sol.wordPattern("aaaa", "dog dog dog dog"))