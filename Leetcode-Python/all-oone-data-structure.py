__author__ = 'Adward'


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        class Row(object):  # double-linked list node
            def __init__(self, val):
                self.val = val
                self.keys = set()
                self.prev = self.suc = None

        indexes = {}  # key(str) -> Row
        head, tail = Row(0), Row(0)
        head.suc, tail.prev = tail, head

        def inc(key):
            """
            Inserts a new key <Key> with value 1. Or increments an existing key by 1.
            :type key: str
            :rtype: void
            """
            row = indexes[key] if key in indexes else tail
            p = row.prev

            if p.val == row.val + 1:
                indexes[key] = p
                p.keys.add(key)
            else:
                nrow = Row(row.val + 1)
                nrow.keys.add(key)
                indexes[key] = nrow
                p.suc = row.prev = nrow
                nrow.prev, nrow.suc = p, row

            if len(row.keys):
                row.keys.remove(key)
            if row != tail and len(row.keys) == 0:
                row.prev.suc, row.suc.prev = row.suc, row.prev  # delete this row

        def dec(key):
            """
            Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
            :type key: str
            :rtype: void
            """
            if key not in indexes:
                return
            row = indexes[key]
            p = row.suc

            if row.val == 1:
                pass
            elif p.val == row.val - 1:
                indexes[key] = p
                p.keys.add(key)
            else:
                nrow = Row(row.val - 1)
                nrow.keys.add(key)
                indexes[key] = nrow
                p.prev = row.suc = nrow
                nrow.prev, nrow.suc = row, p

            if len(row.keys):
                row.keys.remove(key)
                if row.val == 1:
                    del indexes[key]
            if len(row.keys) == 0:
                row.prev.suc, row.suc.prev = row.suc, row.prev  # delete this row

        def getMaxKey():
            """
            Returns one of the keys with maximal value.
            :rtype: str
            """
            for key in head.suc.keys:
                return key
            return ""

        def getMinKey():
            """
            Returns one of the keys with Minimal value.
            :rtype: str
            """
            for key in tail.prev.keys:
                return key
            return ""

        self.inc = inc
        self.dec = dec
        self.getMaxKey = getMaxKey
        self.getMinKey = getMinKey


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
# obj.inc("a")
# obj.inc("b")
# obj.inc("b")
# obj.inc("c")
# obj.inc("c")
# obj.inc("c")
# obj.dec("b")
# obj.dec("b")
# print(obj.getMinKey())
# obj.dec("a")
# print(obj.getMinKey())
# print(obj.getMaxKey())

obj.inc("hello")
obj.inc("hello")
obj.inc("world")
obj.inc("world")
obj.inc("hello")
obj.dec("world")
print(obj.getMaxKey())
print(obj.getMinKey())