# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
回溯 没有剪枝 这种题不容易想到解决方案 不是一眼看出有暴力解决方案求优化的题目
'''

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

    # :type ret: List[str] 保存最终的结果
    # :type path: str 保存单次结果
    # :type num: str
    # :type target: int 最后经过运算生成的目标结果
    # :type pos: int 每次递归的起始下标
    # :type eval: int 到本轮递归为止已经通过运算得出的结果
    # :type multed: int 目前已经等到的str中 从右向左找到第一个非乘号 其右边的算式的值 eg 1+2*3 则multed=2*3=6
    # :rtype
    def DFS(self, ret, path, num, target, pos, eval, multed):
        if pos == len(num):     # 返回条件
            if target == eval:
                ret.append(path)
            return
        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':    # 这句是一定要的 解决cur = int(05) = 5这样的问题
                break
            cur = int(num[pos: i + 1])
            if pos == 0:    # 第一轮特殊考虑 path后不跟符号
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