# -*- coding: UTF-8 -*-
__author__ = 'wang'

import collections

class Solution(object):
    # :type start: str
    # :type end: str
    # :type wordlist: Set[str]
    # :rtype: List[List[int]]
    def findLadders(self, start, end, wordlist):
        toVisit, dist = [], 1
        visited = set()
        level = dict()
        parents = collections.defaultdict(set)
        toVisit.append(start)   # 待访问队列
        while toVisit:
            num = len(toVisit)  # num记录该层的节点数
            for i in range(num):
                word = toVisit.pop(0)
                if word == endWord:
                    # 遇到endWord可以返回
                    return dist
                # 添加word节点的下一层
                for i in range(len(word)):
                    letter = word[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word == endWord:
                            # 剪枝 虽然不在队头 但可以知道已经找到endWord 可以立即返回dist+1
                            return dist + 1
                        if new_word in wordlist:    # 构造成功
                            if new_word not in visited: # 没访问过
                                toVisit.append(new_word)
                                visited.add(new_word)
                                level[new_word] = dist
                            if level[word] != level[new_word]:
                                parents[new_word].add(word)
                    word = word[:i] + letter + word[i + 1:]
            dist += 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])