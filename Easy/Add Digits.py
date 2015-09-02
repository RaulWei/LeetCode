# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
这是一题找规律的数学题
input  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ...
output 0 1 2 3 4 5 6 7 8 9 1  2  3  4  5  6  7  8  9  1  2
公式是d(n) = num%9 == 0 ? (num==0? 0 : 9) : num%9
'''

class Solution(object):
    # :type num: int
    # :rtype: int
    def addDigits(self, num):
        return (0 if num == 0 else 9) if num % 9 == 0 else num % 9

if __name__ == '__main__':
    sol = Solution()
    print(sol.addDigits(19))
    print(sol.addDigits(38))