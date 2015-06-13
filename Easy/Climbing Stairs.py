# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
爬台阶
climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
超时
分析后实际上是斐波那契数列
每个数等于前两个数之和
'''

class Solution:

    def __init__(self):
        self.Fib = [0, 1, 2]
        for i in range(3, 51):
            self.Fib.append(self.Fib[i-2] + self.Fib[i-1])

    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n < 51:
            return self.Fib[n]
        else:
            for i in range(51, n+1):
                self.Fib.append(self.Fib[i-2] + self.Fib[i-1])
            return self.Fib[n]

if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(5))
