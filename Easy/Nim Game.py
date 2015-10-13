# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type n: int
    # :rtype: bool
    def canWinNim(self, n):
        if n & 1 == 0 and (n >> 1) & 1 == 0:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.canWinNim(4))
    print(sol.canWinNim(5))
