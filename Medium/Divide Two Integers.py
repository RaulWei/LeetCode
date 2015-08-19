# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        positive = dividend > 0 and divisor > 0
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
        return min(max(res, -2147483648), 2147483648)
