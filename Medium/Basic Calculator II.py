# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
s只包含空格 数字 加减乘除 没有括号
从左向右扫描 依次处理
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        stk = []
        num, res = 0, 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if not s[i].isdigit() and ' ' != s[i] or i == len(s) - 1:
                if sign == '+':
                    stk.append(num)
                elif sign == '-':
                    stk.append(-1 * num)
                elif sign == '*':
                    stk.append(stk.pop() * num)
                elif sign == '/':
                    dividend = stk.pop()
                    if dividend >= 0:
                        sig = 1
                    else:
                        sig = -1
                    stk.append(abs(dividend) // num * sig)
                sign = s[i]
                num = 0
        while stk:
            res += stk.pop()
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate('14-3/2'))
    print(sol.calculate('3+2*2'))
    print(sol.calculate(' 3/2 '))
    print(sol.calculate(' 3+5 / 2 '))