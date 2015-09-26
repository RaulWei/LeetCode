# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type nums: List[int]
    # :type k: int
    # :type t: int
    # :rtype: bool
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) >= 2:
            for i in range(len(nums)):
                for j in range(i + 1, min(i + k + 1, len(nums))):
                    if abs(nums[j] - nums[i]) <= t:
                        return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([4, 2], 2, 1))
    print(sol.containsNearbyAlmostDuplicate([-1, -1], 1, -1))
    print(sol.containsNearbyAlmostDuplicate([1, 2], 0, 1))
    print(sol.containsNearbyAlmostDuplicate([2, 2], 3, 0))