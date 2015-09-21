# -*- coding: UTF-8 -*-
__author__ = 'wang'

import math

class Solution(object):
    # :type n: int
    # :rtype: int
    def countPrimes(self, n):
        isPrime = [True for i in range(n)]
        for i in range(2, int(math.sqrt(n))):
            if not isPrime[i]:
                continue
            j = i ** 2
            while j < n:
                isPrime[j] = False
                j += i
        ret = []
        for i in range(2, n):
            if isPrime[i]:
                ret.append(i)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(13))