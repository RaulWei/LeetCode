# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type nums: List[int]
    # :rtype: void Do not return anything, modify nums in-place instead.
    def moveZeroes(self, nums):
        seat, i = 0, 0
        while i < len(nums) - seat:
            if nums[i] == 0:
                for j in range(i, len(nums) - seat - 1):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                seat += 1
                i = 0
            else:
                i += 1
        return nums

if __name__ == '__main__':
    sol = Solution()
    print(sol.moveZeroes([0, 0, 1]))
    print(sol.moveZeroes([0, 1, 0, 3, 12]))