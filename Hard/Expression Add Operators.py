# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type num: str
    # :type target: int
    # :rtype: List[str]
    def addOperators(self, num, target):
        if not num:
            return []
        ret = []
        self.DFS(ret, "", num, target, 0, 0, 0)
        return ret

    def DFS(self, ret, path, num, target, pos, eval, multed):
        if pos == len(num):
            if target == eval:
                ret.append(path)
            return
        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            cur = int(num[pos: i + 1])
            if pos == 0:
                self.DFS(ret, path + str(cur), num, target, i + 1, eval + cur, cur)
            else:
                self.DFS(ret, path + '+' + str(cur), num, target, i + 1, eval + cur, cur)
                self.DFS(ret, path + '-' + str(cur), num, target, i + 1, eval - cur, -cur)
                self.DFS(ret, path + '*' + str(cur), num, target, i + 1, eval - multed + multed * cur, multed * cur)

if __name__ == '__main__':
    sol = Solution()
    print(sol.addOperators("123", 6))
    print(sol.addOperators("232", 8))
    print(sol.addOperators("105", 5))
    print(sol.addOperators("00", 0))
    print(sol.addOperators("3456237490", 9191))