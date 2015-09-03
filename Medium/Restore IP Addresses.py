# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
比较普通的回溯法处理 先放置后验证 循环递归
循环条件比较重要 好好理解 这块剪枝不少
'''

class Solution(object):
    # :type s: str
    # :rtype: List[str]
    def restoreIpAddresses(self, s):
        ret, res = [], ''
        self.DFS(1, ret, res, s, 0)
        return ret

    def DFS(self, step, ret, res, s, index):
        if step == 4:
            # 得到一组合理解
            ip = s[index:]
            if self.is_valid(ip):
                res += ip
                ret.append(res)
            return
        i = 1
        while i < 4 and index + i + (4 - step) <= len(s):
            # 循环找合适的位置插入'.' index是上个点的位置 距离不能超过4个字符 并要给下个点留足够位置
            ip = s[index: index + i]
            if self.is_valid(ip):
                res = res + ip + '.'
                self.DFS(step + 1, ret, res, s, index + i)
                res = res.rstrip('.')
                res = res.rstrip(ip)
            i += 1

    def is_valid(self, str):
        if len(str) > 3 or len(str) == 0 or (len(str) > 1 and str[0] == '0') or int(str) > 255:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.restoreIpAddresses("1010815125"))