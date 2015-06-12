# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
计算一个数的阶乘的尾巴有几个0
题解 http://www.cnblogs.com/ganganloveu/p/4193373.html
n/k代表从1到n中能被k整除的个数
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        count = 0
        while n:
            count += n / 5
            n /= 5
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.trailingZeroes(10))
