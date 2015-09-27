# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
把数字转换成英文单词
三个数字为一组 先写一个把三个数字转换为英文单词的函数
'''

class Solution(object):

    table_less20 = [
        "", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
        "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
    table_decade = [
        "", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    ]
    table_level = [
        "", "Thousand", "Million", "Billion"
    ]

    # :type num: int
    # :rtype: str
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        ret, i = [], 0
        while num > 0:
            num_tmp = num % 1000
            num /= 1000
            if num_tmp > 0:
                if i > 0:
                    ret.append(self.numberToWords_less1000(num_tmp) + " " + self.table_level[i])
                else:
                    ret.append(self.numberToWords_less1000(num_tmp))
            i += 1
        ret = ret[::-1]
        if ret[-1] == "":
            ret.pop()
        return ' '.join(ret)

    def numberToWords_less1000(self, num):
        res = []
        # 百位
        tmp = num / 100
        num %= 100
        if tmp > 0:
            res.append(self.table_less20[tmp])
            res.append("Hundred")
        # 十位和个位
        if num <= 20:
            res.append(self.table_less20[num])
        else:
            res.append(self.table_decade[num / 10])
            res.append(self.table_less20[num % 10])
        if res[-1] == "":
            res.pop()
        return ' '.join(res)

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberToWords(1000))
    print(sol.numberToWords(30))
    print(sol.numberToWords(123))
    print(sol.numberToWords(0))
    print(sol.numberToWords(22))
    print(sol.numberToWords(12345))
    print(sol.numberToWords(1234567891))

