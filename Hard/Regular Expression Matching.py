# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
实现正则匹配".*"
参考
http://www.cnblogs.com/flowerkzj/p/3726667.html
http://blog.csdn.net/hcbbt/article/details/44016237
python单单就递归会超时
需要记忆化DP
'''

class Solution:
    dp = {}

    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if (s, p) in self.dp:
            return self.dp[(s, p)]

        if not p:
            return not s

        # P的下一个不是* 则当前必须匹配才有机会让s匹配p
        if len(p) == 1 or p[1] != '*':
            self.dp[(s[1:], p[1:])] = self.isMatch(s[1:], p[1:])
            return len(s) > 0 and (s[0] == p[0] or p[0] == '.') and self.dp[(s[1:], p[1:])]

        # p的下一个是*
        # 当前s和p匹配
        while s and (s[0] == p[0] or p[0] == '.'):
            self.dp[(s, p[2:])] = self.isMatch(s, p[2:])
            if self.dp[(s, p[2:])]:
                return True
            s = s[1:]
        # 当前s和p不匹配
        self.dp[(s, p[2:])] = self.isMatch(s, p[2:])
        return self.dp[(s, p[2:])]

if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch('aab', 'c*a*b'))
    print(sol.isMatch('aa', 'a'))
    print(sol.isMatch('a', '.*..a'))
    print(sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))