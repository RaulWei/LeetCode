# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
设f(n)表示从s[i]到s[len-1]包含s[i]的最长的有效括号匹配子串长度
逆序遍历
初态： f(len-1) = 0
终态： max{f[n]}, 0 <= n < len
递推公式：
if 跳过f[i+1]的下一个字符 == ')' 并且再往后一个 还没有越界
    f(i) = f[i+1] + 2 +f[f[i+1]+2]
http://blog.csdn.net/cfc1243570631/article/details/9304525
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        pass

if __name__ == '__main__':
    sol = Solution()