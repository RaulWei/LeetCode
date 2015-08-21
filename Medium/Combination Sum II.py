# -*- coding: UTF-8 -*-
__author__ = 'weimw'
import copy

'''
返回条件 + 剪枝条件 + 循环套递归
'''

class Solution(object):
    # :type candidates: List[int]
    # :type target: int
    # :rtype: List[List[int]]
    def combinationSum2(self, candidates, target):
        res, path = [], []
        book = [0] * len(candidates)
        candidates.sort()
        self.DFS(target, res, path, candidates, 0, book)
        return res

    # start是为了剪枝 得到都是非递减的答案
    def DFS(self, target, res, path, candidates, start, book):
        if target == 0:
            # 得到一个合法解
            if path not in res:
                res.append(copy.deepcopy(path))
            return True
        if target < 0 or target < candidates[start]:
            # 剪枝条件
            return False
        for i in range(start, len(candidates)):
            if candidates[i] <= target and book[i] == 0:
                path.append(candidates[i])
                book[i] = 1
                self.DFS(target - candidates[i], res, path, candidates, i, book)
                path.pop()
                book[i] = 0
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2([1, 1], 1))
    print(sol.combinationSum2([7], 7))
    print(sol.combinationSum2([8, 7, 4, 3], 11))