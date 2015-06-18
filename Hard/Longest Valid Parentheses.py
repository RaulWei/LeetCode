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
        if not s:
            return 0
        lens = len(s)
        f = [0] * lens
        for i in range(0, lens-1)[::-1]:
            if s[i] == ')':
                # 没有以')'开始的最长有效括号匹配
                f[i] = 0
            else:
                # s[i] == '('
                if i + f[i + 1] + 1 < lens and s[i + f[i + 1] + 1] == ')':
                    # 跳过f[i + 1]个元素 如果下一个是')' 正好可以和'('匹配上 那么+2
                    f[i] = f[i + 1] + 2
                    if i + f[i + 1] + 2 < lens:
                        # 在')'之后可能还有有效匹配 只不过一开始被')'隔开了 现在')'匹配了 自然要把后面的整合进来
                        f[i] += f[i + f[i+1] + 2]
        return max(f)

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses('(((()(()'))