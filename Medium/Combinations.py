# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
基于回溯法框架的修改
生成的组合必须是res[i] > res[i-1]
'''

import copy

class Solution:
    def backtracking(self, res, res_t, step, k, n, book):
        if step == k:
            res_t_c = copy.deepcopy(res_t)
            res.append(res_t_c)
            return
        for i in range(n):
            if book[i] == 0 and (step == 0 or i + 1 > res_t[step - 1]):
                res_t[step] = i + 1
                book[i] = 1
                self.backtracking(res, res_t, step + 1, k, n, book)
                book[i] = 0

    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        res = []
        res_t = [0 for i in range(k)]
        book = [0 for i in range(n)]
        self.backtracking(res, res_t, 0, k, n, book)
        return res

if __name__ == '__main__':
    sol = Solution()
    sol.combine(4, 2)
