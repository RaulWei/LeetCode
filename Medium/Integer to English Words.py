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

    # :type num: int
    # :rtype: str
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        return self.numberToWords_less1000(num)

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
        return ' '.join(res)

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberToWords(0))
    print(sol.numberToWords(22))
    print(sol.numberToWords_less1000(200))
    print(sol.numberToWords_less1000(10))
    print(sol.numberToWords_less1000(998))

