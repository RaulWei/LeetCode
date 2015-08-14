# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[i] != i:
                t = nums[i]
                nums[i] = nums[nums[i]]
                nums[nums[i]] = t
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.firstMissingPositive([3, 4, -1, 1]))