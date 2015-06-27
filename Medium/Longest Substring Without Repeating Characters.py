# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[i]以i结尾的最长非重复字符串长度
初态: f[0] = 1
终态: max{f[i]}, 0 <= i < len(s)
递推公式:
if s[i] not in s[i-1-f[i]: i-1]
    f[i] = f[i-1] + 1
else f[i] =
'''

class Solution:
    # @return {integer} 返回n代表在s中找到ch n为ch下标 如果n为-1表示没找到
    def existCh(self, ch, s, right, length):
        left = right - length + 1
        i = left
        while i <= right:
            if s[i] == ch:
                return i
            i += 1
        return -1

    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        f = [1]
        for i in range(1, len(s)):
            p = self.existCh(s[i], s, i - 1, f[i - 1])
            if p == -1:
                # s[i]可以与之前组成更长的不重复字符串
                f.append(f[i - 1] + 1)
            else:
                f.append(i - p)
        return max(f)

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcabcbb'))
