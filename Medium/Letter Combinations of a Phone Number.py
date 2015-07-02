# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
模拟手机九宫格键盘 输入数字 输出可能的字母组合
不带标记的回溯算法
类似求全排列 比全排列简单
'''

import copy

class Solution:
    # 数字与字母对应的哈希表
    numToCh = [
        [' '], [''], ['a', 'b', 'c'], ['d', 'e', 'f'],
        ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']
    ]

    def backtracking(self, step, digits, res_t, res):
        if step == len(digits):
            # 停止条件
            res_t_cp = copy.deepcopy(res_t)
            res.append(''.join(res_t_cp))
            return
        for i in range(len(self.numToCh[int(digits[step])])):
            res_t[step] = self.numToCh[int(digits[step])][i]
            self.backtracking(step + 1, digits, res_t, res)

    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits:
            return []
        res_t = [0 for i in range(len(digits))]
        res = []
        self.backtracking(0, digits, res_t, res)
        return res

if __name__ == '__main__':
    sol = Solution()
    sol.letterCombinations('23')
