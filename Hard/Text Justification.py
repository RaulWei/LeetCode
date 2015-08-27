# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import copy

class Solution(object):
    # :type words: List[str]
    # :type maxWidth: int
    # :rtype: List[str]
    def fullJustify(self, words, maxWidth):
        i, ret = 0, []
        while i < len(words):
            # 每次处理一行
            line_length, row = 0, []
            while i < len(words):
                line_length += len(words[i]) + 1
                row.append(words[i])
                i += 1
                if line_length - 1 > maxWidth:
                    row.pop()
                    i -= 1
                    break
            ret.append(copy.deepcopy(row))
        return ret

if __name__ == '__main__':
    sol = Solution()
    sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)