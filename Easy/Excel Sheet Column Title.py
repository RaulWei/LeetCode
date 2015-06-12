# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
10进制转换为26进制
* 考虑余数为0的情况 Z为26 AZ为52
'''

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        digit2Letter = ['Z',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G',
                        'H', 'I', 'J', 'K', 'L', 'M', 'N',
                        'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                        'V', 'W', 'X', 'Y']
        r = []
        while n:
            r.append(digit2Letter[n % 26])
            if n % 26 == 0:
                n = n/26-1
            else:
                n /= 26
        return ''.join(r[::-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(28))