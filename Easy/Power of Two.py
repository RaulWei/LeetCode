# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
判断一个数是不是2的幂
如果是的话 那么2进制表示将只有一个1 剩下全是0
'''

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