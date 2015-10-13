# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
每次可取1~3个 最后一次取干净的人胜利
要求判断给定n个石子 我先手的情况下是否能赢
实际上我们可以把n化为2进制看待 只要我们可以通过取子把最后一位和倒数第二位清0
那么我们就赢了
'''

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
