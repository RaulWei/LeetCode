# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
类似3Sum 也是固定一端然后移动剩下两端
时间复杂度O(n^2)
'''

import sys

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        min = sys.maxint
        val = 0
        for i in range(len(nums) - 2):
            low, high = i + 1, len(nums) - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if target == sum:
                    # 找到相等是最接近的 可以直接返回
                    return target
                # 更新min和val
                if min > abs(target - sum):
                    min = abs(target - sum)
                    val = sum
                # 移动low或者high
                if target > sum:
                    low += 1
                else:
                    high -= 1
        return val

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))