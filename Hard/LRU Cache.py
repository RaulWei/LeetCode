# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
注意 这里的key-value对中的key并不是下标的意思
妈的 key还可以一样
'''

class LRUCache(object):

    # 成员变量
    m_map = dict()
    m_capacity = 0
    m_cache = []

    # :type capacity: int
    def __init__(self, capacity):
        self.m_capacity = capacity

    # :rtype: int
    def get(self, key):
        if key not in self.m_map:
            return -1
        self.mov_to_head(key)
        return self.m_map[key][1]
        # return self.m_map[key].val

    # :type key: int
    # :type value: int
    # :rtype: nothing
    def set(self, key, value):
        if key not in self.m_map:
            # 不在map中 则插入新元素
            self.m_cache.insert(0, [key, value])
            self.m_map[key] = [key, value]
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
    lru = LRUCache(1)
    lru.set(2, 1)
    print(lru.get(2))
    lru.set(3, 2)
    print(lru.get(2))
    print(lru.get(3))