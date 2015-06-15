# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
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
            return num1 / num2
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
            while lenStack > 1 and stack[lenStack-1].isdigit() and stack[lenStack-2].isdigit():
                num1 = stack.pop()
                num2 = stack.pop()
                ope = stack.pop()
                r = self.calc(num1, num2, ope)
                stack.append(str(r))
                lenStack = len(stack)
        return int(stack.pop())

if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(['3', '-4', '+']))
