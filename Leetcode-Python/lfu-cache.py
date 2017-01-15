__author__ = 'Adward'
from collections import defaultdict
# from collections import deque
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.key2Freq = defaultdict(int)
        self.key2Time = {}
        self.freq2Key = [set()]
        self.capacity = capacity
        self.t = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        val = self.cache[key]
        f = self.key2Freq[key]
        self.key2Freq[key] += 1
        self.key2Time[key] = self.t
        self.t += 1
        self.freq2Key[f].remove(key)
        f += 1
        if f >= len(self.freq2Key):
            self.freq2Key.append(set())
        self.freq2Key[f].add(key)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self.cache) == self.capacity:
            f = 1
            while len(self.freq2Key[f]) == 0:
                f += 1
            invalid = min(self.freq2Key[f], key=lambda x: self.key2Time[x])
            self.freq2Key[f].remove(invalid)
            del self.key2Freq[invalid]
            del self.cache[invalid]

        self.key2Freq[key] += 1
        self.key2Time[key] = self.t
        self.t += 1
        f = self.key2Freq[key]
        if key in self.cache:
            self.freq2Key[f-1].remove(key)
        self.cache[key] = value
        if f >= len(self.freq2Key):
            self.freq2Key.append(set())
        self.freq2Key[f].add(key)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)