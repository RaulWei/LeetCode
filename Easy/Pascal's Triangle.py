# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
熟悉python二维数组操作
打印杨辉三角形
'''

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0:
            return []
        # 声明二维数组
        tri = [[] for i in range(numRows)]
        tri[0].append(1)
        for i in range(1, numRows):
            tri[i].append(1)
            for j in range(len(tri[i-1]) - 1):
                tri[i].append(tri[i-1][j]+tri[i-1][j+1])
            tri[i].append(1)
        return tri

if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(3))
    print(sol.generate(0))

