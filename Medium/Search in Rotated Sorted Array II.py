# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type nums: List[int]
    # :type target: int
    # :rtype: bool
    def search(self, nums, target):
        if not nums:
            return False
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return True
            # 以下的判断中target都不等于mid
            if nums[low] < nums[mid]:   # 左半边排好序
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:    # 右半边排好序
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # 实际上这里nums[left] == nums[mid] 但是已经排除target == nums[mid]
                # 所以target肯定也不等于nums[left] 可以把这个略过去
                low += 1
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([5, 1, 1, 1, 1, 1], 5))
    print(sol.search([1, 3, 1, 1, 1], 3))