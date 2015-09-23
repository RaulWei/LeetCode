# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
这题自己想的时候又想复杂了  leetcode都刷了200多题了 还是长进很少啊
分治 + 递归
其实想法和这个差不多了 只是更复杂 没有这个清晰
重点是要利用递归的返回是一组结果数 然后利用这些数做相应处理得到最后结果
'''

class Solution(object):
    # :type input: str
    # :rtype: List[int]
    def diffWaysToCompute(self, input):
        ret = []
        for i in range(len(input)):
            if input[i] == '*' or input[i] == '-' or input[i] == '+':   # 题目说只有这三种操作
                left_res = self.diffWaysToCompute(input[:i])
                right_res = self.diffWaysToCompute(input[i + 1:])
                for x in left_res:
                    for y in right_res:
                        ret.append(self.calc(input[i], x, y))
        return ret if ret else [int(input)]

    def calc(self, oper, x, y):
        if oper == '*':
            return x * y
        if oper == '-':
            return x - y
        if oper == '+':
            return x + y

if __name__ == '__main__':
    sol = Solution()
    print(sol.diffWaysToCompute("2*3-4*5"))