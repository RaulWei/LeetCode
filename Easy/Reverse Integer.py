# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
* 考虑0的情况
* 考虑10 100的情况
* 考虑反转后溢出的情况

题目给定的int范围在32位
所以判断溢出用了"r * (r < 2**31)"这样的技巧
'''
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        s = str(x)
        if len(s) == 1:
            return x
        elif s[0].isdigit():
            r = int(s[::-1].lstrip('0'))
            return r * (r < 2**31)
        else:
            r = int(s[:0:-1].lstrip('0'))
            return -1 * r * (r < 2**31)

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(1534236469))
    print(sol.reverse(0))
    print(sol.reverse(10))
    print(sol.reverse(-10))
