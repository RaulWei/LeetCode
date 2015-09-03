# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type s: str
    # :rtype: List[str]
    def restoreIpAddresses(self, s):
        pass

    def is_valid(self, str):
        if len(str) > 3 or len(str) == 0 or (len(str) > 1 and str[0] == '0') or int(str) > 255:
            return False
        return True
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.restoreIpAddresses("1010815125"))