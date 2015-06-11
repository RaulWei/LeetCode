# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n:
            if n % 2 == 1:
                count += 1
            n /= 2
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(0))
