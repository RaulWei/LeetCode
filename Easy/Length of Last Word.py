# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
一组单词以空格分隔
找到最后一个单词 返回它的长度
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.strip(' ')
        list_s = s.split(' ')
        return len(list_s[-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord(' a '))
