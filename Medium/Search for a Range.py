# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
找到有序数组中target数的开始和结束位置
二分法 注意条件判断要精确
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        res = []
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                p = mid
                while p >= 0 and nums[p] == target:
                    p -= 1
                p += 1
                res.append(p)
                # 这时p指向第一个等于target的位置
                while p < len(nums) and nums[p] == target:
                    p += 1
                # 这时p指向第一个不等于target的位置
                res.append(p - 1)
                return res
        # 此时low应该等于high
        if nums[low] == target:
            res.append(low)
        if nums[high] == target:
            res.append(high)
        if not res:
            return [-1, -1]
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([1], 1))
    print(sol.searchRange([2, 2], 2))
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))


