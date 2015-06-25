# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
数学法解格雷码
将二进制转换为格雷码

Binary Code ：1011 要转换成Gray Code
1011 = 1（照写第一位）, 1(第一位与第二位异或 1^0 = 1), 1(第二位异或第三位 0^1=1), 0 (第三位异或第四位 1^1 =0) = 1110
即 (1011 >> 1) ^ 1011 = 1110
'''

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        res = []
        for i in range(2 ** n):
            res.append((i >> 1) ^ i)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.grayCode(1))
