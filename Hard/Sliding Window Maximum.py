# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
建立一个队列deque 存num的下标
建立一个数组ret 存返回结果
queue[0]存当前window中的最大值的下标
'''

class Solution(object):
    # :type nums: List[int]
    # :type k: int
    # :rtype: List[int]
    def maxSlidingWindow(self, nums, k):
        queue, ret = [], []
        for i in range(len(nums)):
            while queue and queue[0] < i - k + 1:
                # 超过window的size 则删除
                queue.pop(0)
            while queue and nums[queue[-1]] < nums[i]:
                # 从右向左把比当前的nums[i]小的都删掉
                queue.pop()
            # 经过前面两步的处理 在这里把当前数添加进队列
            queue.append(i)
            if i >= k - 1:
                ret.append(nums[queue[0]])  # queue[0]存的是当前window中最大值的下标
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))