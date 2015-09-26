# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f(n)代表numSquares
初态：f(0) = 0, f(1) = 1
终态：f(n)
递推公式：
f(n) = min(f(i) + 1 if n - i is perfect square number) 1 <= i < n
'''

class Solution(object):

    f = [0, 1]

    # :type n: int
    # :rtype: int
    def numSquares(self, n):
        lenf = len(self.f)
        while lenf <= n:
            self.f.append(lenf)
            j = 1
            while j * j <= lenf:
                self.f[lenf] = min(self.f[lenf], self.f[lenf - j * j] + 1)
                j += 1
            lenf += 1
        return self.f[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(13))
    print(sol.numSquares(254))
    print(sol.numSquares(266))
    print(sol.numSquares(10000))
    print(sol.numSquares(4635))
    print(sol.numSquares(9975))
    print(sol.numSquares(7691))
