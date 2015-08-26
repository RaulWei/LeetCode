# -*- coding: UTF-8 -*-
__author__ = 'weimw'

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
        return '/' + '/'.join(res)

if __name__ == '__main__':
    sol = Solution()
    print(sol.simplifyPath("/home/"))
    print(sol.simplifyPath("/a/./b/../../c/"))