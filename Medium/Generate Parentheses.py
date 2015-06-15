# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
这题本来应该是回溯法
把括号生成用二叉树表达 然后做树的回溯
但是看了Discuss之后 还是这种写法优雅 不过感觉很难想到
特别是递归函数的参数定义
'''

class Solution:
    # @param {integer} leftNum 已经归位的左括号数
    # @param {integer} rightNum 已经归位的右括号数
    # @param {integer} n
    # @param {List} res 解集合
    # @param {string} tRes 单个解
    def generateRes(self, leftNum, rightNum, n, res, tRes):
        if leftNum == n and rightNum == n:
            res.append(tRes)
        if leftNum < n:
            # 能加左括号的条件是已经归位的左括号个数小于n
            self.generateRes(leftNum + 1, rightNum, n, res, tRes + '(')
        if leftNum > rightNum:
            # 能加右括号的条件是已经归位的右括号个数小于已经归位的左括号个数
            self.generateRes(leftNum, rightNum + 1, n, res, tRes + ')')

    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        res = []
        self.generateRes(0, 0, n, res, '')
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))


