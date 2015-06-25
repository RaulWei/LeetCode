# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
二分法找数组的峰值 O(log n)
本题只存在一个峰值 没有[1, 2, 3, 2, 4, 5, 1]这样的情况
'''

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1
        mid = 0
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < nums[mid + 1]:
                # low = mid 会进入死循环
                low = mid + 1
            else:
                high = mid
        return low

if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3, 1, 2]))

