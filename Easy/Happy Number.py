# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
不断模拟计算
当计算结果为1时判断它为happy number
当计算结果为出现过的数时判断它不是happy number
'''

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        L = [0]
        while(1):
            n = self.computeSumOfSquares(n)
            if n == 1:
                return True
            elif n in L:
                return False
            else:
                L.append(n)

    def computeSumOfSquares(self, n):
        sum = 0
        while(n):
            sum += (n % 10) ** 2
            n /= 10
        return sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.computeSumOfSquares(65))
    print(sol.isHappy(1))

