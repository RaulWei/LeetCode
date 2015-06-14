# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        if not s:
            return 0
        roman2Int = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50,
            'C': 100, 'D': 500,
            'M': 1000
        }
        len_s = len(s)
        sum = 0
        for i in range(len_s - 1):
            if roman2Int[s[i]] >= roman2Int[s[i + 1]]:
                sum += roman2Int[s[i]]
            else:
                sum -= roman2Int[s[i]]
        sum += roman2Int[s[len_s - 1]]
        return sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt('MMCMLXXXVII'))