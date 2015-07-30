# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
给定一个nums数组 求res数组
res[i] = nums所有数的乘积/nums[i]
但是题目规定不能用除法
本题采用双向法
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        res = [0 for n in nums]

        tmp = 1
        for i in range(len(nums)):
            res[i] = tmp
            tmp *= nums[i]

        tmp = 1
        for i in range(0, len(nums))[::-1]:
            res[i] *= tmp
            tmp *= nums[i]

        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))