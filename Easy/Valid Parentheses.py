# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
经典的利用栈进行括号匹配的问题
'''

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0 or match[i] != stack[len(stack)-1]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('[[[]]]]'))
