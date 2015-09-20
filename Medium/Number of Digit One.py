# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
给定一个整数n，计算所有小于等于n的非负整数中数字1出现的次数
http://bookshadow.com/weblog/2015/07/08/leetcode-number-digit-one/

把数n看作   (high_n) cur (low_n), low_c = 10 ** cur位数
cur = 0, high_n: 0 ~ high_n-1, low_n: 0 ~ low_c-1
cur = 1, high_n: 0 ~ high_n-1, low_n: 0 ~ low_c-1 以及 high_n: high, low_n: 0 ~ low_n
cur > 1, high_n: 0 ~ high_n, low_n: 0 ~ low_c-1
'''

class Solution:
    def countDigitOne(self, n):
        high_n, low_n, low_c = n, 0, 1
        one_num = 0
        while high_n > 0:
            cur = high_n % 10
            high_n /= 10
            if cur == 0:
                one_num += high_n * low_c
            elif cur == 1:
                one_num += high_n * low_c
                one_num += low_n + 1
            else:
                one_num += (high_n + 1) * low_c
            low_c *= 10
            low_n = n - high_n * low_c
        return one_num

if __name__ == '__main__':
    sol = Solution()
    print(sol.countDigitOne(11))
    print(sol.countDigitOne(13))