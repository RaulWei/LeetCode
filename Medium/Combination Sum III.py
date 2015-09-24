# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import copy

'''
简单递归回溯
注意返回条件
arr的元素个数为k时 无论如何都得return了 只不过先判断一个sum 如果等于n的话记录ret
'''

class Solution(object):
        # :type k: int
        # :type n: int
        # :rtype: List[List[int]]
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(10)]):     # 规定构成组合的数字只能在[1, 9]之间
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