# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
找出所有从start到end最短的路径
改自Word Ladder 实际上还是BFS层序遍历 把图转换为树 一层一层遍历 触碰到end那么从start到end的路径即最短路径
记录每个节点的父亲节点们 最后从end倒推回去 即可求出所有路径
技巧：用set和defaultdict加速
'''

import collections

class Solution(object):
    # :type start: str
    # :type end: str
    # :type wordlist: Set[str]
    # :rtype: List[List[int]]
    def findLadders(self, start, end, wordlist):
        if not start or not end or not wordlist:
            return None
        if start in wordlist:
            wordlist.remove(start)
        toVisit, dist = [], 1
        visited = set()
        level = collections.defaultdict(int)    # 记录节点所在的层 初始化为0
        parents = collections.defaultdict(set)  # 记录节点的父亲节点们 初始化为空集合
        toVisit.append(start)   #
        wordlist.add(end)
        while toVisit:
            num = len(toVisit)  # num记录该层的节点数
            for i in range(num):
                word = toVisit.pop(0)
                # 添加word节点的下一层
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in wordlist:    # 构造成功
                            if new_word not in visited: # 没访问过
                                toVisit.append(new_word)
                                visited.add(new_word)
                                level[new_word] = dist
                            if level[word] < level[new_word]:
                                parents[new_word].add(word)
            dist += 1   # 从start到此的dist+1 实际上也就是层数+1

        # 由end向start构造路径
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res


if __name__ == "__main__":
    sol = Solution()
    # sol.findLadders("a", "c", set(["a", "b", "c"]))
    # sol.findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))