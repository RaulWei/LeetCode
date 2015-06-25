# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
二分
注意边界条件 防止死循环
'''

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        # 先确定在哪一行
        low = 0
        high = len(matrix) - 1
        while high > low:
            mid = (low + high) / 2
            if target < matrix[mid][0]:
                high = mid - 1
            else:
                if low == mid:
                    break
                low = mid
        if matrix[high][0] <= target:
            row = high
        else:
            row = low
        # 确定target是否在row行中
        low = 0
        high = len(matrix[row]) - 1
        while high >= low:
            mid = (low + high) / 2
            if target < matrix[row][mid]:
                high = mid - 1
            elif target == matrix[row][mid]:
                return True
            else:
                low = mid + 1
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
    print(sol.searchMatrix([[1], [3]], 3))
