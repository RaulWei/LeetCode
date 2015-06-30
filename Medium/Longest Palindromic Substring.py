# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
马拉车算法 时间复杂度O(N)
详解：http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
'''

class Solution:
    # @return {string} 预处理字符串
    # 例如 abcd -> ^#a#b#c#d#$ 这样把奇偶回文统一到奇数回文
    def preProcess(self, s):
        ret = '^'
        for ch in s:
            ret = ret + '#' + ch
        ret += '#$'
        return ret

    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s:
            return ''
        T = self.preProcess(s)
        P = [0 for i in range(len(T))]
        C, R = 0, 0
        # 构造P数组
        for i in range(1, len(T) - 1):
            # 根据对称性质得到P[i] 提速的关键
            i_mirror = 2 * C - i
            if R > i:
                if P[i_mirror] <= R - i:
                    P[i] = P[i_mirror]
                else:
                    P[i] = R - i

            # 以i为中心扩展回文
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # 移动对称中心C的位置 以及右边界位置
            if i + P[i] > R:
                C = i
                R = i + P[i]

        # 从P数组中找最大回文
        max, center = 0, 0
        for i in range(1, len(T) - 1):
            if max < P[i]:
                max = P[i]
                center = i
        begin, end = (center - 1 - max)/2, (center - 1 - max)/2 + max
        return s[begin:end:]

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('dabccbad'))