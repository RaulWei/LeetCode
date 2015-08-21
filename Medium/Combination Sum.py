# -*- coding: UTF-8 -*-
__author__ = 'weimw'
import copy

class Solution(object):
    # :type candidates: List[int]
    # :type target: int
    # :rtype: List[List[int]]
    def combinationSum(self, candidates, target):
        res, path = [], []
        candidates.sort()
        self.DFS(target, res, path, candidates, 0)
        return res

    def DFS(self, target, res, path, candidates, start):
        if target == 0:
            # 得到一个合法解
            res.append(copy.deepcopy(path))
            return True
        if target < 0 or target < candidates[start]:
            # 剪枝条件
            return False
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                path.append(candidates[i])
                self.DFS(target - candidates[i], res, path, candidates, i)
                path.pop()
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([7], 7))
    print(sol.combinationSum([8, 7, 4, 3], 11))