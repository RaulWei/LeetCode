# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type s: str
    # :type t: str
    # :rtype: str
    def minWindow(self, s, t):
        if not s or not t:
            return ''
        left, right, min_left, min_right = 0, 0, 0, 0
        min_len, min_index, found_num = len(s), 0, 0
        t_num, window_num = [0 for col in range(256)], [0 for col in range(256)]
        is_found = False

        for ch in t:
            t_num[int(ch)] += 1

        for i in range(len(s)):
            # 先找到包含所有t字符的大窗口
            while i < len(s) and found_num < len(t):
                if window_num[int(s[i])] < t_num[int(s[i])]:
                    found_num += 1
                window_num[int(s[i])] += 1
                i += 1
            # 找到大窗口后减小窗口
            if found_num == len(t):
                is_found = True
                min_right = i - 1