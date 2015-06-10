# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
找规律的题目
Z字形打印

0     6       12
1   5 7    11 13
2 4   8 10
3     9

以上应该打印出 0 6 12 1 5 7 11 13 2 4 8 10 3 9
'''

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        i = 0
        res = ''
        sub = []
        while i < len(s):
            # 先构造出第0行记录在sub里
            res += s[i]
            sub.append(i)
            i += 2*numRows-2
        for j in range(1, numRows):
            # 接下来每行都根据第0行构造
            for k in sub:
                if k+j < len(s):
                    res += s[k+j]
                if k+2*numRows-2-j < len(s) and k+j != k+2*numRows-2-j:
                    res += s[k+2*numRows-2-j]
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.convert('PAYPALISHIRING',3))
    print(sol.convert('A', 1))
