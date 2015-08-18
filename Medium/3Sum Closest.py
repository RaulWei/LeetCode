# -*- coding: UTF-8 -*-
__author__ = 'weimw'
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
                    return target
                # 更新min
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