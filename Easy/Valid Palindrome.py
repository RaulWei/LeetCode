# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
判断字符串是否回文
跳过空格和标点符号
只有字母和数字是合法的
规定空字符串也属于回文
'''


class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if s == '' or s == ' ':
            return True
        head = 0
        tail = len(s) - 1
        while 1:
            while not s[head].isalnum():
                head += 1
                if head >= tail:
                    return True
            while not s[tail].isalnum():
                tail -= 1
                if tail <= head:
                    return True
            if s[head].lower() != s[tail].lower():
                return False
            else:
                head += 1
                tail -= 1
            if head >= tail:
                return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome('A man, a plan, a canal: Panama'))
    print(sol.isPalindrome('race a car'))
    print(sol.isPalindrome(''))
    print(sol.isPalindrome('0'))
    print(sol.isPalindrome('aa'))
    print(sol.isPalindrome(" "))
    print(sol.isPalindrome('.'))
