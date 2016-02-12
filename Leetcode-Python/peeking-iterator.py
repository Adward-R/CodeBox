__author__ = 'Adward'
# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = [n for n in reversed(nums)]

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if len(self.nums):
            return True
        else:
            return False

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        tmp = self.nums[-1]
        self.nums.pop()
        return tmp

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        if self.iterator.hasNext():
            self.cache = self.iterator.next()
        else:
            self.cache = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        tmp = self.cache
        if self.iterator.hasNext():
            self.cache = self.iterator.next()
        else:
            self.cache = None
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cache is not None:
            return True
        else:
            return False

# Your PeekingIterator object will be instantiated and called as such:
nums = [1,2,3]
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    print(val)
    print(iter.next())         # Should return the same value as [val].