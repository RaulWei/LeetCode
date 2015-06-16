# -*- coding: UTF-8 -*-
__author__ = 'Wang'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSum(self, cur, tStr, sum):
        if not cur:
            pass
        elif not cur.left and not cur.right:
            tStr += str(cur.val)
            sum.append(int(tStr))
        else:
            self.getSum(cur.left, tStr + str(cur.val), sum)
            self.getSum(cur.right, tStr + str(cur.val), sum)

    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        sum = []
        self.getSum(root, '', sum)
        res = 0
        for i in sum:
            res += i
        return res


if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p6 = TreeNode(6)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6

    sol = Solution()
    print(sol.sumNumbers(None))
