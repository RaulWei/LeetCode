# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        MAX, flag = 0, 0
        for i in range(len(nums)):
            if MAX < nums[i]:
                MAX = nums[i]
            if nums[i] == 0:
                for j in range(max(i-MAX, 0), i):
                    if nums[j] > i - j or (nums[j] == i - j and i == len(nums) - 1):
                        flag = 1
                        break
                if flag == 1:
                    flag = 0
                else:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump([2, 3, 1, 1, 4]))
    print(sol.canJump([3, 2, 1, 0, 4]))
    print(sol.canJump([2, 0, 0]))
