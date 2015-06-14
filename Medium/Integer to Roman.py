# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
阿拉伯数字转换为罗马数字
将每位数字按区间分析 1-3 4 5 6-8 9
'''

class Solution:

    # @param {integer} num
    # @return {string}
    def getNumLen(self, num):
        if num > 999:
            return 4
        elif num > 99:
            return 3
        elif num > 9:
            return 2
        return 1

    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        len_num = self.getNumLen(num)
        res = []
        while len_num:
            digit = num / (10 ** (len_num - 1))
            if 0 < digit < 4:
                # 第一次用列表生成式 萌萌哒
                res += [roman[2 * len_num - 2] for i in range(digit)]
            elif digit == 4:
                res.append(roman[2 * len_num - 2])
                res.append(roman[2 * len_num - 1])
            elif digit == 5:
                res.append(roman[2 * len_num - 1])
            elif 5 < digit < 9:
                res.append(roman[2 * len_num - 1])
                res += [roman[2 * len_num - 2] for i in range(digit-5)]
            elif digit == 9:
                res.append(roman[2 * len_num - 2])
                res.append(roman[2 * len_num])
            num %= (10 ** (len_num - 1))
            len_num -= 1
        return ''.join(res)

if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(1999))
    print(sol.intToRoman(3058))
