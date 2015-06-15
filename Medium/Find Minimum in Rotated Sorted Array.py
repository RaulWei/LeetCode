# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
这题甚至比一些easy题还要easy
从一个升序但是旋转后的数组中找最小的数
遍历数组 只要找到比前一个数小的那个就是
如果找不到 那么就返回第一个数
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums:
            return 0
        len_nums = len(nums)
        for i in range(len_nums-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2, 3]))
