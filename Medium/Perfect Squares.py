# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import math

'''
f(n)代表numSquares
初态：f(0) = 0, f(1) = 1
终态：f(n)
递推公式：
f(n) = min(f(i) + 1 if n - i is perfect square number) 1 <= i < n
'''

class Solution(object):
    # :type n: int
    # :rtype: int
    def numSquares(self, n):
        f = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                f[i] = min(f[i], f[i - j * j] + 1)
                j += 1
        return f[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(13))
    print(sol.numSquares(254))
    print(sol.numSquares(266))
    print(sol.numSquares(9975))