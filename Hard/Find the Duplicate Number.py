# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type nums: List[int]
    # :rtype: int
    def findDuplicate(self, nums):
        low, high = 1, len(nums) - 1
        while low < high:
            mid =(low + high) / 2
            count = 0
            for n in nums:
                count += 1 if n <= mid else 0
            if count > mid:
                # [1, mid]之间有>mid个数 那么鸽巢原理可知其中必有重复
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([1, 2, 3, 4, 5, 3]))