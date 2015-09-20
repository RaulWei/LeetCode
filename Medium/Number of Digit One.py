# -*- coding: UTF-8 -*-
__author__ = 'weimw'

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