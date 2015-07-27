# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
0 <= m <= n <= 2**31
位运算
'''

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        res = 0
        for i in range(0, 32)[::-1]:
            t = 1
            k = m
            while k < n + 1:
                t &= k >> i & 1
                k += 1
                if t == 0:
                    break
            res = (res << 1) | t
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.rangeBitwiseAnd(5, 7))
    print(sol.rangeBitwiseAnd(54, 117))
    print(sol.rangeBitwiseAnd(0, 2147483647))
    print(sol.rangeBitwiseAnd(600000000, 2147483645))
