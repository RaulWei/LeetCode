# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
split处理path得到pathList 对每个pathList中的content
1 等于空或者'.' 什么都不做
2 等于'..' 弹出栈顶
3 等于其他 入栈
'''

class Solution(object):
    # :type path: str
    # :rtype: str
    def simplifyPath(self, path):
        res = []
        pathList = path.split('/')
        for content in pathList:
            if not content or content == '.':
                continue
            if content == ".." and res:
                res.pop()
            elif content != "..":
                res.append(content)
        return '/' + '/'.join(res)  # '/'.join(res)表示'/'夹在每个res成员中间

if __name__ == '__main__':
    sol = Solution()
    print(sol.simplifyPath("/../"))
    print(sol.simplifyPath("/home/"))
    print(sol.simplifyPath("/a/./b/../../c/"))