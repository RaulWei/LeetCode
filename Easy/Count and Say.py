# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n <= 0:
            return '1'
        r = '1'
        for i in range(1, n):
            r = self.next(r)
        return r

    def next(self, s):
        # 计算s的下一个数
        i = 1
        r = ''
        while i <= len(s):
            count = 1
            while i != len(s) and s[i] == s[i-1]:
                count += 1
                i += 1
            r += str(count)
            r += s[i-1]
            i += 1
        return r

if __name__ == '__main__':
    sol = Solution()
    print(sol.next('221'))
    print(sol.countAndSay(-1))
    print(sol.countAndSay(0))
    print(sol.countAndSay(1))
    print(sol.countAndSay(3))
