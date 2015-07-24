# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    def containOne(self, n):
        n_str = str(n)
        count = 0
        for i in range(len(n_str)):
            if n_str[i] == '1':
                count += 1
        return count

    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        count = 0
        for num in range(n+1):
            count += self.containOne(num)
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.countDigitOne(13))