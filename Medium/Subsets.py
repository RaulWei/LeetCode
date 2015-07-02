# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import copy

class Solution:
    def backtracking(self, step, nums, book, res_t, res):
        if step == len(nums):
            res_t_cp = copy.deepcopy(res_t)
            res_t_cp.remove('')
            res.append(res_t_cp)
            return
        for i in range(len(nums)):
            if book[i] == 0:
                res_t[step] = nums[i]
                if nums[i] != '':
                    book[i] = 1
                self.backtracking(step + 1, nums, book, res_t, res)
                book[i] = 0

    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.append('')
        book = [0 for i in range(len(nums))]
        res_t = [0 for i in range(len(nums))]
        res = []
        self.backtracking(0, nums, book, res_t, res)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
