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
            for j in range(i):
                f[i] = min(f[j] + 1, f[i]) if self.isPerfectSquareNumber(i - j) else f[i]
        return f[n]

    def isPerfectSquareNumber(self, num):
        tmp = int(math.sqrt(num))
        return tmp * tmp == num

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(13))
    print(sol.numSquares(254))
    print(sol.numSquares(266))