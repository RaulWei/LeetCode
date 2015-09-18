# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type numerator: int
    # :type denominator: int
    # :rtype: str
    def fractionToDecimal(self, numerator, denominator):
        res, last_numerator, flag = "", -1, 0
        while True:
            shang = numerator / denominator
            # res.append(shang)
            if not res:
                res += str(shang)
                res += '.'
            else:
                res += str(shang)
            numerator = (numerator - denominator * shang) * 10
            if numerator == last_numerator:
                flag = 1
                tmp = res[-1]
                res = res[:-1] + '(' + tmp + ')'
                break
            if numerator == 0:
                if res[-1] == '.':
                    res = res[:-1]
                flag = 2
                break
            last_numerator = numerator
        if flag == 1:   # 循环小数
            pass
        if flag == 2:   # 能够整除
            pass
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(1, 99))
    # sol.fractionToDecimal(20, 30)
    # sol.fractionToDecimal(1, 3)
    # sol.fractionToDecimal(1, 2)
    # sol.fractionToDecimal(2, 1)