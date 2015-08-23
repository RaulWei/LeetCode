# -*- coding: UTF-8 -*-
__author__ = 'weimw'
import copy

# :type nums: List[int]
# :rtype: List[List[int]]
class Solution(object):
    def permuteUnique(self, nums):
        book = [0 for i in range(len(nums))]
        res_t = [0 for i in range(len(nums))]
        res = []
        self.backtracking(0, nums, res_t, res, book)
        return res

    def backtracking(self, step, nums, res_t, res, book):
        if step == len(nums):
            tmp = copy.deepcopy(res_t)
            if tmp not in res:
                res.append(tmp)
            return
        for i in range(len(nums)):
            if book[i] == 0:
                res_t[step] = nums[i]
                book[i] = 1
                self.backtracking(step + 1, nums, res_t, res, book)
                book[i] = 0

if __name__ == '__main__':
    sol = Solution()
    sol.permuteUnique([1, 1, 2])