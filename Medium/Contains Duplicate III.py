# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import sys

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
        if k < 1 or t < 0:
            return False
        bucket, min_value = dict(), -1 * sys.maxint - 1
        for i in range(len(nums)):
            value = nums[i] - min_value
            key = value / (t + 1)
            if bucket.has_key(key) or (bucket.has_key(key - 1) and abs(bucket[key - 1] - value) <= t) or (bucket.has_key(key + 1) and abs(bucket[key + 1] - value) <= t):
                # 若是符合 只可能存在于同一个bucket 或者 相邻bucket中
                return True
            if len(bucket) >= k:
                # 能进这个判断 说明之前k个元素各自进入不同bucket 否则早就return True了
                # 题目要求i和j之间最大间距是k 所以到这里要把i - k的元素从bucket里拿掉
                last_bucket = (nums[i - k] - min_value) / (t + 1)
                bucket.pop(last_bucket)
            bucket[key] = value
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([4, 2], 2, 1))
    print(sol.containsNearbyAlmostDuplicate([-1, -1], 1, -1))
    print(sol.containsNearbyAlmostDuplicate([1, 2], 0, 1))
    print(sol.containsNearbyAlmostDuplicate([2, 2], 3, 0))