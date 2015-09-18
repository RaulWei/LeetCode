# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type numerator: int
    # :type denominator: int
    # :rtype: str
    def fractionToDecimal(self, numerator, denominator):
        res, last_numerator, flag = "", dict(), 0
        if numerator == 0:
            return 0
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        while True:
            shang = numerator / denominator
            if not res or (len(res) == 1 and res[0] == '-'):
                res += str(shang)
                res += '.'
            else:
                res += str(shang)
            numerator = (numerator - denominator * shang) * 10
            if numerator in last_numerator:
                loc = last_numerator[numerator]
                res = res[:loc] + '(' + res[loc:] + ')'
                break
            if numerator == 0:
                if res[-1] == '.':
                    res = res[:-1]
                break
            last_numerator[numerator] = len(res)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(1, 99))
    print(sol.fractionToDecimal(20, 30))
    print(sol.fractionToDecimal(1, 3))
    print(sol.fractionToDecimal(1, 2))
    print(sol.fractionToDecimal(2, 1))