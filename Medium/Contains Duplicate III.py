# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
这题自己想不出来 看了题解自己还想了好久
其实主要用到一个bucket 只不过bucket的宽度设宽了 取t + 1
bucket, key: (num[i] - MIN_VALUE) / (t + 1), value: num[i] - MIN_VALUE
引入MIN_VALUE是用来兼容num中出现负数的情况
'''

class Solution(object):
    # :type nums: List[int]
    # :type k: int
    # :type t: int
    # :rtype: bool
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        pass

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([4, 2], 2, 1))
    print(sol.containsNearbyAlmostDuplicate([-1, -1], 1, -1))
    print(sol.containsNearbyAlmostDuplicate([1, 2], 0, 1))
    print(sol.containsNearbyAlmostDuplicate([2, 2], 3, 0))