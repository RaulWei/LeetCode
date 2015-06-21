# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
终于A了 用例挺厉害的
比如： 1.0, 1; 01,1; 1.2,1.10; 1.1,1.01.0
'''

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        # 初始化-统一拥有小数点
        if '.' not in version1:
            version1 += '.0'
        if '.' not in version2:
            version2 += '.0'
        ver_1 = version1.split('.')
        ver_2 = version2.split('.')
        # 初始化-统一两版本小数点个数
        len_1 = len(ver_1)
        len_2 = len(ver_2)
        if len_1 < len_2:
            lens = len_2
            for i in range(len_2 - len_1):
                ver_1.append('0')
        else:
            lens = len_1
            for i in range(len_1 - len_2):
                ver_2.append('0')
        # 判断每个小数点分隔的部分大小
        i = 0
        while i < lens:
            if int(ver_1[i]) > int(ver_2[i]):
                return 1
            elif int(ver_1[i]) < int(ver_2[i]):
                return -1
            else:
                i += 1
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.compareVersion('1.1', '1.01.0'))
