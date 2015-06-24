# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
二进制的方法 O(n)
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
