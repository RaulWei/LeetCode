# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
不能使用乘法 除法 取模来计算两数除法
被除数不断减去除数 TLE
对除数左移 相当于每次减去2^k个除数 提高速度
'''

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp_divs, i = divisor, 1
            while dividend >= tmp_divs:
                dividend -= tmp_divs
                res += i
                i <<= 1
                tmp_divs <<= 1
        res = res if positive else -res
        # python处理防止溢出实在是太方便了
        return min(max(res, -2147483648), 2147483647)

if __name__ == '__main__':
    sol = Solution()
    print(sol.divide(-1, -1))