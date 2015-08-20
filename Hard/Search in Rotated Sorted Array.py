# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
旋转后的有序数组还是可以用二分法找target
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            # 以下的判断中target都不等于mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([4, 5, 6, 7, 1, 2, 3], 4))