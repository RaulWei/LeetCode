# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
长度为n的数组走马灯向右旋转k次
技巧：前n-k个求逆 后k个求逆 最后整体求逆
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        k %= len(nums)
        # 题目要求不引入新变量 等号左边要写成nums[:]
        # 切片 索引和步长都是负数则从右向左 索引和步长都是正数则从左向右
        nums[:] = nums[-k-1::-1] + nums[-1:-k-1:-1]
        nums[:] = nums[::-1]
        return

if __name__ == '__main__':
    sol = Solution()
    print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))
    print(sol.rotate([1, 2], 3))