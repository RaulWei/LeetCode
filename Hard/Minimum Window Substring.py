# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
滑动窗口法 细节很难处理
参考算法 http://m4tiku.duapp.com/report?pid=85
'''

class Solution(object):
    # :type s: str
    # :type t: str
    # :rtype: str
    def minWindow(self, s, t):
        if not s or not t:
            return ''
        left, min_left, min_right = 0, 0, 0
        min_len, min_index, found_num = len(s), 0, 0
        t_num, window_num = [0 for col in range(256)], [0 for col in range(256)]
        is_found = False

        # 初始化t的字符统计数组
        for ch in t:
            t_num[ord(ch)] += 1

        i = 0
        while i < len(s):
            # 先找到包含所有t中字符的大窗口
            while i < len(s) and found_num < len(t):
                if window_num[ord(s[i])] < t_num[ord(s[i])]:
                    found_num += 1
                window_num[ord(s[i])] += 1
                i += 1
            # 找到大窗口后减小窗口
            if found_num == len(t):
                is_found = True
                min_right = i - 1
                while left < min_right:
                    # 收缩窗口左边 找min_left
                    if window_num[ord(s[left])] > t_num[ord(s[left])]:
                        window_num[ord(s[left])] -= 1
                        left += 1
                    else:
                        break
                min_left = left
                # 找到本轮的最小窗口 更新min_index min_len
                if min_len > min_right - min_left + 1:
                    min_len = min_right - min_left + 1
                    min_index = min_left
                # 找下一轮
                window_num[ord(s[min_left])] -= 1
                found_num -= 1
                left = min_left + 1
        if is_found:
            return s[min_index:min_index + min_len]
        return ''

if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))