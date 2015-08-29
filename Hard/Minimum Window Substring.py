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
            t_num[ord(ch)] += 1

        for i in range(len(s)):
            # 先找到包含所有t字符的大窗口
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
                    if window_num[ord(s[left])] > t_num[ord(s[left])]:
                        window_num[ord(s[left])] -= 1
                        left += 1
                    else:
                        break
                min_left = left
                if min_len > min_right - min_left + 1:
                    min_len = min_right - min_left + 1
                    min_index = min_left
                window_num[ord(s[left])] -= 1
                found_num -= 1
                left += 1
        if is_found:
            return s[min_index:min_len]
        return ''

if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))