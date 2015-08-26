# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type nums: List[int]
    # :rtype: int
    def missingNumber(self, nums):
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([0, 1, 3]))
