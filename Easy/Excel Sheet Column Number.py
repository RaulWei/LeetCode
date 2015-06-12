# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
26进制转换为10进制
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        letter2Digit = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26
        }
        sum = 0
        l_s = len(s)
        for i in range(l_s):
            sum += 26**(l_s-i-1)*letter2Digit[s[i].upper()]
        return sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.titleToNumber('AB'))
