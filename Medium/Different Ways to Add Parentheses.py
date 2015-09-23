# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type input: str
    # :rtype: List[int]
    def diffWaysToCompute(self, input):
        ret = []
        for i in range(len(input)):
            if input[i] == '*' or input[i] == '-' or input[i] == '+':
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