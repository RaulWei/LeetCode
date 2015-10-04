# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
鸽巢原理
给定n + 1个元素 每个元素的范围是[1, n] 肯定有重复的元素 要求找出这个元素
'''

class Solution(object):
    # :type nums: List[int]
    # :rtype: int
    def findDuplicate(self, nums):
        low, high = 1, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            count = 0
            for n in nums:
                count += 1 if low <= n <= mid else 0
            if count > mid - low + 1:
                # [low, mid]之间有 > mid - low + 1个数 那么鸽巢原理可知其中必有重复
                high = mid
            else:
                # [mid + 1, high]之中必有重复
                low = mid + 1
        return low

if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([1, 2, 3, 4, 5, 3]))