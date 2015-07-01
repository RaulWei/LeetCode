# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
实现正则匹配".*"
参考 http://www.cnblogs.com/flowerkzj/p/3726667.html
'''

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not p:
            return not s
        if len(p) >= 2:
            # P的下一个不是*
            if p[1] != '*':
                if s[0] == p[0] or (p[0] == '.' and s):
                    return self.isMatch(s[1::], p[1::])
            # p的下一个是*
            while s and (s[0] == p[0] or (p[0] == '.' and s)):
                if self.isMatch(s, p[2::]):
                    return True
                s = s[1::]
            return self.isMatch(s, p[2::])
        if s == p or p == '.':
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    # print(sol.isMatch('aab', 'c*a*b'))
    print(sol.isMatch('aa', 'a*'))
    print(sol.isMatch('a', '.*..a*'))
