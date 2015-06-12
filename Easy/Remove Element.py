# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
双指针
一个指向原数组 一个指向更新数据(i - rm)
返回更新数组长度
但也需要修改原数组
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        length = len(nums)
        rm = 0
        for i in range(length):
            if nums[i] == val:
                rm += 1
            else:
                nums[i - rm] = nums[i]
        return length - rm

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement([3,3], 3))
