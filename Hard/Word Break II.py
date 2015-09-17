# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type s: str
    # :type wordDict: Set[str]
    # :rtype: List[str]
    def wordBreak(self, s, wordDict):
        ret, res = [], []
        self.backtracking(ret, res, s, wordDict, 0)
        return ret

    def backtracking(self, ret, res, s, wordDict, start):
        if start == len(s):
            str = ' '.join(res)
            ret.append(str)
            return True
        for i in range(start, len(s) + 1)[::-1]:
            if s[i:] in wordDict:
                break
            elif i == start and start != len(s):
                # res = []
                return False
        for i in range(start, len(s) + 1):
            if s[start: i] in wordDict:
                res.append(s[start: i])
                # if self.backtracking(ret, res, s, wordDict, i):
                #     res.pop()
                # else:
                #     return
                self.backtracking(ret, res, s, wordDict, i)
                res.pop()
        return True

if __name__ == '__main__':
    sol = Solution()
    sol.wordBreak("aaaaaaa", set(["aaaa", "aaa"]))
    sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",set(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    sol.wordBreak("catsanddog", set(["cat", "cats", "and", "sand", "dog"]))
