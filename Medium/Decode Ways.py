# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f(n)表示从0到n一共有f(n)种解释
初始：f(0)=1,f(1)=1or2
终态：f(n)
递推公式：f(n)=f(n-1) or f(n)=f(n-1)+f(n-2)
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s:
            return 0
        if len(s) == 1:
            return 1
        f = [1] * len(s)
        if int(s[0:2]) < 27:
            f[1] = 2
        for i in range(3, len(s)):
            if int(s[i-2:i]) < 27:
                f[i] = f[i-1] + f[i-2]
            else:
                f[i] = f[i-1]
        return f[len(s) - 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings('12'))