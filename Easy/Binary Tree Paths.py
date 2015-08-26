# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
简单的DFS 非回溯
'''

import copy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type root: TreeNode
    # :rtype: List[str]
    def binaryTreePaths(self, root):
        if not root:
            return []
        res, tmp = [], []
        ret = []
        self.DFS(root, res, tmp)
        self.processRet(res, ret)
        return ret

    def DFS(self, root, res, tmp):
        if not root:
            return
        if not root.left and not root.right:
            # root是叶子节点 处理返回
            tmp.append(root.val)
            res.append(copy.deepcopy(tmp))
            tmp.pop()
            return
        if root.val != '#':
            tmp.append(root.val)
            root.val = '#'
            self.DFS(root.left, res, tmp)
            self.DFS(root.right, res, tmp)
        tmp.pop()
        return

    def processRet(self, res, ret):
        for r in res:
            s = ''
            for num in r:
                s += str(num) + '->'
            ret.append(s[:-2])

if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(5)
    p1.left = p2
    p1.right = p3
    p2.right = p4
    sol = Solution()
    sol.binaryTreePaths(p1)