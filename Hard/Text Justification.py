# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
本题倒是没有考察什么数据结构
算是一道稍微复杂和麻烦点的模拟题
'''

import copy

class Solution(object):
    # :type words: List[str]
    # :type maxWidth: int
    # :rtype: List[str]
    def fullJustify(self, words, maxWidth):
        i, ret = 0, []
        while i < len(words):
            # 每次处理一行 得到该行包括的单词 存在row中
            line_length, line_word_length, row = 0, 0, []
            while i < len(words):
                line_length += len(words[i]) + 1
                line_word_length += len(words[i])
                row.append(words[i])
                i += 1
                if line_length - 1 > maxWidth:
                    line_word_length -= len(row[-1])
                    row.pop()
                    i -= 1
                    break

            # 处理行list 生成行str 加到ret中
            row_str = ''
            if i == len(words):
                # 最后一行 特殊处理
                row_str = ' '.join(row)
                if maxWidth - len(row_str) > 0:
                    row_str += ' ' * (maxWidth - len(row_str))
            else:
                # 普通行 计算插入空格 组成str
                if len(row) != 1:
                    # 该行有多个单词
                    mean_space = (maxWidth - line_word_length) / (len(row) - 1)
                    extra_space = (maxWidth - line_word_length) % (len(row) - 1)
                    for k in range(len(row) - 1):
                        row_str += row[k] + ' ' * mean_space
                        if k < extra_space:
                            row_str += ' '
                    row_str += row[-1]
                else:
                    # 该行只有一个单词
                    row_str = row[0] + ' ' * (maxWidth - len(row[0]))

            ret.append(copy.deepcopy(row_str))
        return ret

if __name__ == '__main__':
    sol = Solution()
    sol.fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
    sol.fullJustify(["a","b","c","d","e"], 1)
    sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)