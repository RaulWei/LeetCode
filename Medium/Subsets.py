# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
求集合的所有子集
对于集合中的每个元素 都存在两种可能：选 or 不选
'''

import copy

class Solution:
    def backtracking(self, step, nums, res_t, res):
        if step == len(nums):
            # 停止条件
            res_t_cp = copy.deepcopy(res_t)
            res.append(res_t_cp)
            return

        # 选
        res_t.append(nums[step])
        self.backtracking(step + 1, nums, res_t, res)
        # 不选
        res_t.remove(nums[step])
        self.backtracking(step + 1, nums, res_t, res)

    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        res_t, res = [], []
        # 按照递增顺序排列
        nums.sort()
        self.backtracking(0, nums, res_t, res)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
