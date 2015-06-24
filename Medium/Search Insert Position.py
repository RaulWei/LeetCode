# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
给定一个有序数组和待插入数字 找到插入的位置
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if not nums:
            return None
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))
    print(sol.searchInsert([1, 3, 5, 6], 2))
    print(sol.searchInsert([1, 3, 5, 6], 7))
    print(sol.searchInsert([1, 3, 5, 6], 0))
