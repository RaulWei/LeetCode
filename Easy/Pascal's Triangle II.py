# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
类双指针思想
一个指向结果行 一个指向当前行
结果行是当前行的上一行
不用记录所有的结果
'''

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        res = [1]
        for i in range(1, rowIndex+1):
            cur = []
            for j in range(1, i):
                cur.append(res[j-1] + res[j])
            res = [1] + cur + [1]
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(1))
