# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
从最后开始往前遍历是解本题的技巧
遇到数字先存入数字栈中
遇到空格跳过
遇到'('开始一系列处理
遇到非'('的符号先存入符号栈中
'''

class Solution:
    def calc(self, stkNum, stkChar):
        v1 = stkNum.pop()
        v2 = stkNum.pop()
        ch = stkChar.pop()
        if ch == '+':
            stkNum.append(v1 + v2)
        elif ch == '-':
            stkNum.append(v1 - v2)
        return

    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        stkNum, stkChar = [], []
        lenth = len(s)
        num = ''
        for i in range(0, lenth)[::-1]:
            if '0' <= s[i] <= '9':
                num = s[i] + num
                if i - 1 < 0 or s[i-1] < '0' or s[i-1] > '9':
                    stkNum.append(int(num))
                    num = ''
            elif s[i] == '(':
                while stkChar[-1] != ')':
                    self.calc(stkNum, stkChar)
                stkChar.pop()
            elif s[i] == ' ':
                continue
            else:
                stkChar.append(s[i])
        while stkChar:
            # 直到把stkChar栈清空为止
            self.calc(stkNum, stkChar)
        return stkNum[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate('(1+(4+5+2)-3)+(6+8)'))
