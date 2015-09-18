# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
模拟除法得到小数形式的结果
注意几种情况：
1 结果为0
2 符号
3 循环小数
'''

class Solution(object):
    # :type numerator: int
    # :type denominator: int
    # :rtype: str
    def fractionToDecimal(self, numerator, denominator):
        # 初始化 判0 确定符号 统一处理
        res, last_numerator = "", dict()
        if numerator == 0:
            return "0"
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)

        # 循环处理
        while True:
            shang = numerator / denominator
            if not res or (len(res) == 1 and res[0] == '-'):
                res += str(shang)
                res += '.'
            else:
                res += str(shang)
            numerator = (numerator - denominator * shang) * 10
            if numerator in last_numerator: # 无限循环小数
                loc = last_numerator[numerator]
                res = res[:loc] + '(' + res[loc:] + ')'
                break
            if numerator == 0:  # 非循环小数
                if res[-1] == '.':
                    res = res[:-1]
                break
            # last_numerator记录上次被除数numerator出现的时候res到哪一位
            # 如果numerator再次出现则说明小数有循环
            last_numerator[numerator] = len(res)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(1, 99))
    print(sol.fractionToDecimal(20, 30))
    print(sol.fractionToDecimal(1, 3))
    print(sol.fractionToDecimal(1, 2))
    print(sol.fractionToDecimal(2, 1))
    print(sol.fractionToDecimal(-2, 1))
    print(sol.fractionToDecimal(1, -99))