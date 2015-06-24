# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
求全排列
回溯法框架 啊哈算法上的解题方法
'''

import copy

class Solution:
    def backtracking(self, step, nums, res_t, res, book):
        if step == len(nums):
            # 停止条件
            res_t_cp = copy.deepcopy(res_t) # python的传值拷贝
            res.append(res_t_cp)
            return
        for i in range(len(nums)):
            if book[i] == 0:
                # 表示i还没有用过
                res_t[step] = nums[i]
                book[i] = 1
                self.backtracking(step + 1, nums, res_t, res, book)
                book[i] = 0

    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        book = [0 for i in range(len(nums))]
        res_t = [0 for i in range(len(nums))]
        res = []
        self.backtracking(0, nums, res_t, res, book)
        return res

if __name__ == '__main__':
    sol = Solution()
    sol.permute([1, 2, 3])

