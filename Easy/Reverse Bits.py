# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
input 43261596 -> 00000010100101000001111010011100
output 964176192 -> 00111001011110000010100101000000
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ori = str(bin(n)).lstrip('0b')
        sum = 0
        for i in range(len(ori)):
            sum += 2**(i+32-len(ori))*(ori[i] == '1')
        return sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseBits(8))
