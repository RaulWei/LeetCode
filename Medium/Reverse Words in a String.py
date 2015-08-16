# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
巧妙利用了python的列表生成式 list和str转换 split函数 strip函数特性
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ''.join([r + ' ' for r in s.split(' ')[::-1] if r]).strip(' ')

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("   a   b "))
    print(sol.reverseWords('the sky is blue'))
    print(sol.reverseWords('1 '))
