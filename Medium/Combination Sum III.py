# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import copy

class Solution(object):
        # :type k: int
        # :type n: int
        # :rtype: List[List[int]]
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(10)]):
            return []
        ret = []
        self.DFS(k, n, 1, ret, [])
        return ret

    def DFS(self, k, n, cur, ret, arr):
        # ret记录最后的结果 arr记录当前结果
        if len(arr) == k:
            if sum(arr) == n:
                ret.append(copy.deepcopy(arr))
            return
        for i in range(cur, 10):
            arr.append(i)
            self.DFS(k, n, i + 1, ret, arr)
            arr.pop()

if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum3(3, 7))
    print(sol.combinationSum3(3, 9))