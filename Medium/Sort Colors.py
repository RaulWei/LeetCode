# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type nums: List[int]
    # :rtype: void Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        red_idx, blue_idx = 0, len(nums) - 1
        idx = 0
        while idx <= blue_idx:
            if nums[idx] == 0:  # red
                nums[idx], nums[red_idx] = nums[red_idx], nums[idx]
                red_idx += 1
                idx += 1
            elif nums[idx] == 2:  # blue
                nums[idx], nums[blue_idx] = nums[blue_idx], nums[idx]
                blue_idx -= 1
            elif nums[idx] == 1:  # white
                idx += 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.sortColors([0]))
    print(sol.sortColors([1, 2, 0, 1, 0, 0]))