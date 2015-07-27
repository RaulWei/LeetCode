# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
0 <= m <= n <= 2**31
只要m!=n 那么从m到n的求and最低位必为0
把m和n都向右移 直到m等于n
'''

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        step = 0
        while m != n:
            m >>= 1
            n >>= 1
            step += 1
        return m << step

if __name__ == '__main__':
    sol = Solution()
    print(sol.rangeBitwiseAnd(5, 7))
    print(sol.rangeBitwiseAnd(54, 117))
    print(sol.rangeBitwiseAnd(0, 2147483647))
    print(sol.rangeBitwiseAnd(600000000, 2147483645))
    print(sol.rangeBitwiseAnd(33, 45))
