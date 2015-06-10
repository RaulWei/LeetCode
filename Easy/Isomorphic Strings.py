# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
* 单向对应
a对应b的同时b不一定对应a

* 不能多对一
a对应a b就不能再对应a
'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        hashMap = {}
        for i in range(len(s)):
            if hashMap.has_key(s[i]):
                if hashMap[s[i]] != t[i]:
                    return False
            else:
                # 不能多对一
                for j in hashMap:
                    if hashMap[j] == t[i]:
                        return False
                hashMap[s[i]] = t[i]
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic('egg','add'))
    print(sol.isIsomorphic('paper','title'))
    print(sol.isIsomorphic('foo','bar'))
    print(sol.isIsomorphic('ab','aa'))
