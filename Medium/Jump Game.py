# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        MAX, flag = 0, 0
        for i in range(len(nums)):
            if MAX < nums[i]:
                MAX = nums[i]
            if nums[i] == 0:
                for j in range(i-MAX, i):
                    if nums[j] > i - j:
                        flag = 1
                        break
                if flag == 1:
                    flag = 0
                else:
                    return False
        return True

