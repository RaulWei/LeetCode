# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        version1 = '0' + version1.lstrip('0')
        version2 = '0' + version2.lstrip('0')
        if '.' not in version1:
            version1 += '.0'
        if '.' not in version2:
            version2 += '.0'
        ver_1 = version1.split('.')
        ver_2 = version2.split('.')
        len_1 = len(ver_1)
        len_2 = len(ver_2)
        if len_1 < len_2:
            for i in range(len_2 - len_1):
                ver_1.append('0')
        else:
            for i in range(len_1 - len_2):
                ver_2.append('0')
        i = 0
        while i < len_1 and i < len_2:
            if int(ver_1[i]) > int(ver_2[i]):
                return 1
            elif int(ver_1[i]) < int(ver_2[i]):
                return -1
            else:
                i += 1
        if len_1 == len_2:
            return 0
        elif len_1 > len_2:
            return 1
        else:
            return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.compareVersion('1.1', '1.01.0'))
