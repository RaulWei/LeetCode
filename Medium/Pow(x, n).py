# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
二进制的方法 大大提高速度
参考 http://blog.csdn.net/fengbingyang/article/details/12236121
'''

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow(x, -1 * n)
        res = 1.0
        while n:
            if n & 1 > 0:
                res *= x
            x *= x
            n >>= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.myPow(10, -2))
