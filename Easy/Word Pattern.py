# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
pattern与str中的word必须一一对应 所以我这里开两个dict
'''

class Solution(object):
    # :type pattern: str
    # :type str: str
    # :rtype: bool
    def wordPattern(self, pattern, str):
        dic1, dic2 = dict(), dict()
        stri = str.split()
        if len(stri) != len(pattern):   # 长度不一致 直接False
            return False
        for i in range(len(pattern)):
            if pattern[i] in dic1 and dic1[pattern[i]] != stri[i]:  # pattern对应stri
                return False
            if stri[i] in dic2 and dic2[stri[i]] != pattern[i]: # stri对应pattern
                return False
            dic1[pattern[i]] = stri[i]
            dic2[stri[i]] = pattern[i]
        return True

if  __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))
    print(sol.wordPattern("abba", "dog dog dog dog"))