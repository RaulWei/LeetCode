# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
统计小于n的素数的个数
Sieve of Eratosthenes 算法
'''

import math

class Solution(object):
    # :type n: int
    # :rtype: int
    def countPrimes(self, n):
        if n < 2:
            return 0
        isPrime = [True for i in range(n)]
        count = n - 2
        for i in range(2, int(math.sqrt(n)) + 1):
            if not isPrime[i]:
                continue
            j = i ** 2
            while j < n:
                if isPrime[j]:
                    isPrime[j] = False
                    count -= 1
                j += i
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(0))
    print(sol.countPrimes(1))
    print(sol.countPrimes(2))
    print(sol.countPrimes(3))
    print(sol.countPrimes(5))
    print(sol.countPrimes(13))
    print(sol.countPrimes(120))
    print(sol.countPrimes(1500000))