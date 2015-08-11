# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if int(num1) == 0 or int(num2) == 0:
            return '0'
        lens1 = len(num1)
        lens2 = len(num2)
        res = [0] * (lens1 + lens2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        c = 0
        for i in range(lens1):
            for j in range(lens2):
                r = int(num1[i]) * int(num2[j]) + c + res[i + j]
                c = r / 10
                res[i + j] = r % 10
            if c != 0:
                res[i + j + 1] += c
                c /= 10
        return ''.join(str(e) for e in res)[::-1].lstrip('0')

if __name__ == '__main__':
    sol = Solution()
    print(sol.multiply('9999', '99'))
    print(sol.multiply('1', '1'))