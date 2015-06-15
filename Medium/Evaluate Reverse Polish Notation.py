# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
逆波兰表达式求值
从后往前遍历
数字 运算符入栈 如果栈顶依次是数字数字运算符
则将这三者出栈计算后再把数字入栈 循环

注意
1 数字会有正负数
2 除法运算
'''

import re
import operator

class Solution:
    def isDigit(self, num):
        # 正则匹配正负数
        if re.match(r"[+-]?\d+", num):
            return True
        return False

    def str2Int(self, str):
        try:
            num = int(str)
        except:
            num = -1 * int(str[1])
        return num

    def calc(self, num1, num2, ope):
        num1 = int(num1)
        num2 = int(num2)
        if ope == '+':
            return num1 + num2
        elif ope == '-':
            return num1 - num2
        elif ope == '*':
            return num1 * num2
        elif ope == '/':
            # 这里要用精确除法 否则测试用例报错
            return int(operator.truediv(num1, num2))
        elif ope == '%':
            return num1 % num2

    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        stack = []
        lens = len(tokens)
        for i in range(0, lens)[::-1]:
            stack.append(tokens[i])
            lenStack = len(stack)
            while lenStack > 1 and self.isDigit(stack[lenStack-1]) and self.isDigit(stack[lenStack-2]):
                num1 = stack.pop()
                num2 = stack.pop()
                ope = stack.pop()
                r = self.calc(num1, num2, ope)
                stack.append(str(r))
                lenStack = len(stack)
        return int(stack.pop())

if __name__ == '__main__':
    sol = Solution()
    #print(sol.isDigit('383'))
    #print(sol.str2Int('-100'))
    print(sol.evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']))
