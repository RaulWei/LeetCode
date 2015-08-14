# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                t = nums[i]
                nums[i] = nums[t-1]
                nums[t-1] = t
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

if __name__ == '__main__':
    sol = Solution()
    print(sol.firstMissingPositive([3, 4, -1, 1]))
    print(sol.firstMissingPositive([1, 1]))