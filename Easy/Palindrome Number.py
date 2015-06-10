# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        s = str(x)
        # list切片技巧实现字符串反转
        if s == s[::-1]:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(11211))
    print(sol.isPalindrome(-1))
    print(sol.isPalindrome(10))