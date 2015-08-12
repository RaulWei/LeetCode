# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
利用字典和序列
'''

class Solution:
    # @param {string[]} strs
    # @return {string[][]}
    def groupAnagrams(self, strs):
        if not strs:
            return []
        dic, res = {}, []
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in dic:
                res[dic[sorted_str]].append(str)
            else:
                dic[sorted_str] = len(dic)
                res.append([str])
        for r in res:
            r = r.sort()
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
