# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
测试用例
前缀包括空格 正负号 0
中间包含字母
'''

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if not str:
            return 0
        s = str
        # 确定符号
        s = s.lstrip(' ')
        sign = 1
        if s[0] == '+':
            sign = 1
            s = s.strip('+')
        if s[0] == '-':
            sign = -1
            s = s.strip('-')
        if s[0] == '+':
            s = s.strip('+')
        # 删除前缀0
        s = s.lstrip(' ')
        s = s.lstrip('0')
        if not s:
            return 0
        l_s = len(s)
        r = 0
        toNum = {
            '0': 0, '1': 1,
            '2': 2, '3': 3,
            '4': 4, '5': 5,
            '6': 6, '7': 7,
            '8': 8, '9': 9,
        }
        for i in range(l_s):
            r += 10**(l_s-i-1)*toNum[s[i]]*sign
        return r

if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi('0000'))
    print(sol.myAtoi('0'))
    print(sol.myAtoi('00100'))
    print(sol.myAtoi('12300'))
    print(sol.myAtoi('+0'))
    print(sol.myAtoi(''))
    print(sol.myAtoi('+-2'))
    print(sol.myAtoi('-+1'))
