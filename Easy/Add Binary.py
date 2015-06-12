# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
二进制加法
11 + 10 = 101
'''

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        p1 = a[::-1]
        p2 = b[::-1]
        r = []
        carry = 0
        l_max = max(len(a), len(b))
        l_min = min(len(a), len(b))
        for i in range(l_max):
            if i < l_min:
                t = int(p1[i]) + int(p2[i]) + carry
            else:
                if len(a) < len(b):
                    t = 0 + int(p2[i]) + carry
                else:
                    t = int(p1[i]) + 0 + carry
            if t == 0:
                r.append('0')
            elif t == 1:
                r.append('1')
                carry = 0
            elif t == 2:
                r.append('0')
                carry = 1
            else:
                r.append('1')
                carry = 1
        if carry == 1:
            r.append('1')
        # list to str
        return ''.join(r[::-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary('0', '0'))
