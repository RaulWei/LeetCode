# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n >= 0:
            sum = 0
            while n:
                sum += n & 1
                n >>= 1
            if sum == 1:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(2))
    print(sol.isPowerOfTwo(6))