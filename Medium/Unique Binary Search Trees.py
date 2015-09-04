# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
 F(N)表示N个节点共可以有F(N)种BST摆法
 Taking 1~n as root respectively:
      1 as root: # of trees = F(0) * F(n-1)  // F(0) == 1
      2 as root: # of trees = F(1) * F(n-2)
      3 as root: # of trees = F(2) * F(n-3)
      ...
      n-1 as root: # of trees = F(n-2) * F(1)
      n as root:   # of trees = F(n-1) * F(0)

 So, the formulation is:
      F(n) = F(0) * F(n-1) + F(1) * F(n-2) + F(2) * F(n-3) + ... + F(n-2) * F(1) + F(n-1) * F(0)
'''
class Solution(object):
    # :type n: int
    # :rtype: int
    def numTrees(self, n):
        f = [0 for col in range(n + 1)]
        f[0], f[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                f[i] += f[j] * f[i - j - 1]
        return f[n]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(3))