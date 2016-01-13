__author__ = 'Adward'
class LRUCache(object):
    class KeyTreeNode(object):
        def __init__(self, key, value):
            self.value = value
            self.key = key
            self.left = None
            self.right = None
            self.before = None
            self.after = None
            self.active = True

        def deactivate(self):
            self.active = False
            self.before = self.after = None

        def connect(self, node):
            """
            :type node: KeyTreeNode
            """
            self.after = node
            node.before = self

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.used = 0
        self.root = None
        self.lru = None
        self.last = None

    def makeLast(self, node):
        self.last.connect(node)
        self.last = node
        self.last.after = None

    def get(self, key):
        """
        :rtype: int
        """
        if self.used:
            p = self.root
            while p:
                if key < p.key:
                    p = p.left
                elif key > p.key:
                    p = p.right
                else:
                    if p.active:
                        if p.after:
                            if p.before:
                                p.before.connect(p.after)
                            else:  #no before, p is the lru
                                self.lru = p.after
                                self.lru.before = None
                            self.makeLast(p)
                        return p.value
                    else:
                        return -1
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if not self.root: #first node
            self.root = self.KeyTreeNode(key, value)
            self.lru = self.root
            self.last = self.root
            self.used = 1
        else: #go find the key
            p = self.root
            pre = None
            while p:
                if key < p.key:
                    pre = p
                    p = p.left
                elif key > p.key:
                    pre = p
                    p = p.right
                else:
                    p.value = value
                    if p.active:
                        if p.after:
                            if p.before:
                                p.before.connect(p.after)
                            else:  #no before, p is the lru
                                self.lru = p.after
                                self.lru.before = None
                            self.makeLast(p)
                    else:
                        p.active = True
                        self.makeLast(p)
                        if self.used < self.capacity:
                            self.used += 1
                        else:
                            tmp = self.lru.after
                            self.lru.deactivate()
                            self.lru = tmp
                            self.lru.before = None
                    break

            if not p:
                if key < pre.key:
                    pre.left = self.KeyTreeNode(key, value)
                    self.last.connect(pre.left)
                    self.last = pre.left
                else:
                    pre.right = self.KeyTreeNode(key, value)
                    self.last.connect(pre.right)
                    self.last = pre.right
                if self.used < self.capacity:#normal insertion
                    self.used += 1
                else:
                    tmp = self.lru.after
                    self.lru.deactivate()
                    self.lru = tmp
                    self.lru.before = None

lruCache = LRUCache(1)
lruCache.set(1, 11)
lruCache.set(2, 22)
print(lruCache.get(1))

'''
def disp(lruCache):
    node = lruCache.lru
    while node:
        print(str(node.key) + ' | ' + str(node.value))
        node = node.after

lruCache = LRUCache(10)

lruCache.set(10,13)
lruCache.set(3,17)
lruCache.set(6,11)
lruCache.set(10,5)
lruCache.set(9,10)
lruCache.get(13)
lruCache.set(2,19)
lruCache.get(2)
lruCache.get(3)
lruCache.set(5,25)
lruCache.get(8)
lruCache.set(9,22)
lruCache.set(5,5)
lruCache.set(1,30)
lruCache.get(11)
lruCache.set(9,12)
lruCache.get(7)
lruCache.get(5)
lruCache.get(8)
lruCache.get(9)
lruCache.set(4,30)
lruCache.set(9,3)
lruCache.get(9)
lruCache.get(10)
lruCache.get(10)
lruCache.set(6,14)
lruCache.set(3,1)
lruCache.get(3)
lruCache.set(10,11)
lruCache.get(8)
lruCache.set(2,14)
lruCache.get(1)
lruCache.get(5)
lruCache.get(4)
lruCache.set(11,4)
lruCache.set(12,24)
#print(lruCache.used)
lruCache.set(5,18)
lruCache.get(13)
lruCache.set(7,23)
lruCache.get(8)
lruCache.get(12)
lruCache.set(3,27)
lruCache.set(2,12)
lruCache.get(5)
lruCache.set(2,9)
lruCache.set(13,4)
lruCache.set(8,18)
lruCache.set(1,7)
lruCache.get(6)
lruCache.set(9,29)
lruCache.set(8,21)
lruCache.get(5)
lruCache.set(6,30)
lruCache.set(1,12)
lruCache.get(10)
lruCache.set(4,15)
lruCache.set(7,22)
lruCache.set(11,26)
lruCache.set(8,17)
lruCache.set(9,29)
lruCache.get(5)
lruCache.set(3,4)
lruCache.set(11,30)
lruCache.get(12)
lruCache.set(4,29)
lruCache.get(3)
lruCache.get(9)
lruCache.get(6)
lruCache.set(3,4)
lruCache.get(1)
lruCache.get(10)
lruCache.set(3,29)
lruCache.set(10,28)
lruCache.set(1,20)
lruCache.set(11,13)
lruCache.get(3)
lruCache.set(3,12)
lruCache.set(3,8)
lruCache.set(10,9)
lruCache.set(3,26)
lruCache.get(8)
lruCache.get(7)
lruCache.get(5)
lruCache.set(13,17)
lruCache.set(2,27)
lruCache.set(11,15)
lruCache.get(12)
lruCache.set(9,19)
lruCache.set(2,15)
lruCache.set(3,16)
lruCache.get(1)
lruCache.set(12,17)
lruCache.set(9,1)
lruCache.set(6,19)
lruCache.get(4)
lruCache.get(5)
lruCache.get(5)
lruCache.set(8,1)
lruCache.set(11,7)
lruCache.set(5,2)
lruCache.set(9,28)
lruCache.get(1)
lruCache.set(2,2)
lruCache.set(7,4)
lruCache.set(4,22)
lruCache.set(7,24)
lruCache.set(9,26)
lruCache.set(13,28)
lruCache.set(11,26)
disp(lruCache)
'''