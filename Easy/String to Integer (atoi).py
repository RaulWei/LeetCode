# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
测试用例
前缀包括空格 正负号 0
中间包含字母

最后还是看了解题报告来做
用了正则表达式
没想到我越想越复杂的事情
别人几行代码就搞定了
不过人家用了库嘛
一开始以为int()是不能用的
'''
import re

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        try:
            str = str.strip()
            str = re.match(r'^[+-]?\d+', str).group()
            num = int(str)
            return min((1<<31)-1, max(-(1<<31), num))
        except: return 0

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
    print(sol.myAtoi('-3'))
