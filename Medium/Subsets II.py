# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
Subsets是对某个元素 选 or 不选 的问题
本题对于重复元素是 不选 or 选一次 or ... or 选n次 的问题
'''

import copy

class Solution(object):
    def backtracking(self, step, nums, res_t, res):
        if step == len(nums):
            # 停止条件
            res_t_cp = copy.deepcopy(res_t)
            res.append(res_t_cp)
            return

        # 计算元素重复几次
        idx, count = step, 1
        while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
            count += 1
            idx += 1

        for n in range(count + 1):  # 选的次数
            for k in range(n):
                res_t.append(nums[step])
            self.backtracking(step + count, nums, res_t, res)
            for k in range(n):
                res_t.remove(nums[step])

    # :type nums: List[int]
    # :rtype: List[List[int]]
    def subsetsWithDup(self, nums):
        res_t, res = [], []
        # 按照递增顺序排列
        nums.sort()
        self.backtracking(0, nums, res_t, res)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup([1, 2, 2]))