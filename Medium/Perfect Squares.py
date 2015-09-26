# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f(n)代表numSquares
初态：f(i) = i
终态：f(n)
递推公式：
f(n) = min(f(n), f(n - j * j) + 1), j * j <= n

普通DP会超时 这里用static DP加速
'''

class Solution(object):

    # 之前的写法是在__init__中定义self.f 这样一直超时
    # python声明static的正确做法应该是如下 直接在class下初始变量
    # 在__init__中定义的话只有在实例化类的时候才能构建
    # OJ可能实例化多个类 如下的写法可以保证多个类共用一个static变量f 这样才是加速
    f = [0, 1]

    # :type n: int
    # :rtype: int
    def numSquares(self, n):
        lenf = len(self.f)
        while lenf <= n:
            self.f.append(lenf)
            j = 1
            while j * j <= lenf:
                self.f[lenf] = min(self.f[lenf], self.f[lenf - j * j] + 1)
                j += 1
            lenf += 1
        return self.f[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(13))
    print(sol.numSquares(254))
    print(sol.numSquares(266))
    print(sol.numSquares(10000))
    print(sol.numSquares(4635))
    print(sol.numSquares(9975))
    print(sol.numSquares(7691))
