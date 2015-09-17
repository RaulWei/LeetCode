# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
注意 这里的key-value对中的key并不是下标的意思
python类中的成员变量的初始化应该放在__init__中
如果像注释的代码一样放在外面 可能本地不会出错 但是交到OJ上会出现莫名其妙的错误
'''

class LRUCache(object):

    # 成员变量
    # m_map = {}
    # m_capacity = 0
    # m_cache = []

    # :type capacity: int
    def __init__(self, capacity):
        self.m_capacity = capacity
        self.m_cache = []
        self.m_map = dict()

    # :rtype: int
    def get(self, key):
        if key not in self.m_map:
            return -1
        self.mov_to_head(key)
        return self.m_map[key][1]

    # :type key: int
    # :type value: int
    # :rtype: nothing
    def set(self, key, value):
        if key not in self.m_map:
            # 不在map中 则插入新元素
            self.m_cache.insert(0, [key, value])
            self.m_map[key] = self.m_cache[0]   # map的key对应的指向cache对应项（类似于引用 修改一处则两处都变）
            if len(self.m_cache) > self.m_capacity:
                erase = self.m_cache.pop()
                self.m_map.pop(erase[0])
        else:
            self.m_map[key][1] = value
            self.mov_to_head(key)

    def mov_to_head(self, key):
        item = self.m_map[key]
        self.m_cache.remove(item)
        self.m_cache.insert(0, item)

if __name__ == '__main__':
    lru = LRUCache(2)
    print(lru.get(2))
    lru.set(2, 6)
    print(lru.get(1))
    lru.set(1, 5)
    lru.set(1, 2)
    print(lru.get(1))
    print(lru.get(2))

