# -*- coding: UTF-8 -*-
__author__ = 'weimw'


class Solution(object):
    # :type s: str
    # :rtype: bool
    def isNumber(self, s):
        invalid, space, sign, digit, dot, exponent = range(6)
        transTable = [
            # 0invalid 1space 2sign 3digit 4dot 5exponent
            [-1, 0, 3, 1, 2, -1],    # 0 初始无输入或者只有space的状态
            [-1, 8, -1, 1, 4, 5],   # 1 输入数字后
            [-1, -1, -1, 4, -1, -1],    # 2 前面没有数字 只输入.后的状态
            [-1, -1, -1, 1, 2, -1],     # 3 输入了符号
            [-1, -1, -1, 4, -1, 5],     # 4 前面有数字和.
            [-1, -1, 6, 7, -1, -1],     # 5 输入了e或者E
            [-1, -1, -1, 7, -1, -1],    # 6 输入了e或者E后输入符号
            [-1, 8, -1, 7, -1, -1],     # 7 输入了e或者E后输入数字
            [-1, 8, -1, -1, -1, -1],    # 8 有效输入后输入空格
        ]

        state = 0
        for ch in s:
            inputType = invalid
            if ch == ' ':
                inputType = space
            elif ch == '+' or ch == '-':
                inputType = sign
            elif '0' <= ch <= '9':
                inputType = digit
            elif ch == '.':
                inputType = dot
            elif ch == 'e' or ch == 'E':
                inputType = exponent
            state = transTable[state][inputType]
            if state == -1:
                return False
        if state == 1 or state == 4 or state == 7 or state == 8:
            return True
        return False
