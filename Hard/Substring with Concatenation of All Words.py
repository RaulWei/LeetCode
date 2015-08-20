# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
勉强AC
注意words可以包含重复的word
http://bangbingsyb.blogspot.jp/2014/11/leetcode-substring-with-concatenation.html
以上的思路和我很像 可以参考
'''

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        res, dic = [], {}
        word_num, word_len = len(words), len(words[0])
        # 初始化 建立字典
        for i in range(word_num):
            if words[i] not in dic:
                dic[words[i]] = 1
            else:
                dic[words[i]] += 1
        # 遍历s 找到符合的索引
        for i in range(len(s) - word_len * word_num + 1):
            if self.isivalid(i, s, word_num, word_len, dic):
                res.append(i)
        return res

    def isivalid(self, i, s, word_num, word_len, dic):
        # 本来令local_dic = copy.deepcopy(dic)然后做相应判断 这样开销太大 TLE
        k, local_dic = 0, {}
        while k < word_num:
            word = s[i + word_len * k: i + word_len * (k + 1)]
            if word not in dic:
                return False
            if word in local_dic:
                local_dic[word] += 1
                if local_dic[word] > dic[word]:
                    return False
            else:
                local_dic[word] = 1
            k += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(sol.findSubstring("aaaa", ["a", "a", "a"]))