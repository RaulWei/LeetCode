# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
把数字转换成英文单词
三个数字为一组 先写一个把三个数字转换为英文单词的函数
'''

class Solution(object):

    table = [
        "", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

    # :type num: int
    # :rtype: str
    def numberToWords(self, num):
        pass

    def numberToWords_less1000(self, num):
        res = []
        # 百位
        tmp = num / 100

