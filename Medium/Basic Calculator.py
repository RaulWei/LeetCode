# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
从最后开始往前遍历
'''

class Solution:
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
                pass
            elif s[i] == ' ':
                continue
            else:
                stkChar.append(s[i])

if __name__ == '__main__':
    sol = Solution()
