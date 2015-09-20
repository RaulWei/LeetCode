# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
从字符串中找10个字符为一组重复出现的子字符串
利用字典轻松搞定
'''

class Solution(object):
    # :type s: str
    # :rtype: List[str]
    def findRepeatedDnaSequences(self, s):
        letter_long = 10
        dic = dict()
        for i in range(len(s) - letter_long + 1):
            if s[i:i + letter_long] not in dic:
                dic[s[i:i + letter_long]] = 0
            else:
                dic[s[i:i + letter_long]] += 1
        ret = []
        for d in dic:
            if dic[d] > 0:
                ret.append(d)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAAAAAAAA"))
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))