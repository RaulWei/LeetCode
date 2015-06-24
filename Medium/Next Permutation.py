# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
求下一排列
找规律题
'''

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if not nums:
            return
        len_nums = len(nums)
        # 从后往前 找到第一个nums[i-1] < nums[i]的 此时nums[i]到nums[n-1]是单调递减
        i = len_nums - 1
        while 0 <= i - 1 and nums[i - 1] >= nums[i]:
            i -= 1
        # 从nums[n-1]到nums[i]找到第一个比nums[i-1]大的
        j = len_nums - 1
        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1
        # 交换刚才定位的i和j
        t = nums[i - 1]
        nums[i - 1] = nums[j]
        nums[j] = t
        # 将nums[n-1]到nums[i]重新排序
        nums[i: len_nums] = sorted(nums[i: len_nums])
        print(nums)


if __name__ == '__main__':
    sol = Solution()
    sol.nextPermutation([5, 1, 1])
