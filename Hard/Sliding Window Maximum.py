# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
建立一个队列deque 存num的下标
建立一个数组ret 存返回结果
'''

class Solution(object):
    # :type nums: List[int]
    # :type k: int
    # :rtype: List[int]
    def maxSlidingWindow(self, nums, k):
        queue, ret = [], []
        for i in range(len(nums)):
            while queue and queue[0] < i - k + 1:
                queue.pop(0)
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ret.append(nums[queue[0]])
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))