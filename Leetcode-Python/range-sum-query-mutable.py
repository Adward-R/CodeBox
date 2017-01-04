__author__ = 'Adward'

class NumArray0(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dif = [0]
        ssum = 0
        for n in nums:
            ssum += n
            self.dif.append(ssum)
        self.leng = len(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.dif[i+1] + self.dif[i]
        for j in range(i+1, self.leng+1):
            self.dif[j] += diff

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if 0 <= i <= j < self.leng:
            return self.dif[j+1]-self.dif[i]
        else:
            return 0

###
class SegTreeNode(object):
    def __init__(self, start, end, sum=0):  # inclusive
        self.start, self.end, self.sum = start, end, sum
        self.left, self.right = None, None

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        def build(node):
            s, e = node.start, node.end
            if s == e:
                node.sum = nums[s]
            else:
                mid = (s + e) // 2
                node.left = SegTreeNode(s, mid)
                node.right = SegTreeNode(mid+1, e)
                node.sum = build(node.left) + build(node.right)
            return node.sum

        self.N = len(nums)
        self.segTree = None
        if self.N:
            self.segTree = SegTreeNode(0, self.N-1)
            build(self.segTree)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def recRangeFind(node, i, val):
            s, e = node.start, node.end
            diff = (val - node.sum) if s == e else (
                recRangeFind(node.left, i, val) if i <= ((s + e) // 2) else recRangeFind(node.right, i, val))
            node.sum += diff
            return diff

        if 0 <= i < self.N:
            recRangeFind(self.segTree, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def recSumRange(node, i, j):
            s, e = node.start, node.end
            if i == s and j == e:
                return node.sum
            mid = (s + e) // 2
            if j <= mid:
                return recSumRange(node.left, i, j)
            elif i > mid:
                return recSumRange(node.right, i, j)
            else:
                return recSumRange(node.left, i, mid) + recSumRange(node.right, mid+1, j)

        if not self.segTree or i > j:
            return 0
        i, j = max(0, i), min(self.N-1, j)
        return recSumRange(self.segTree, i, j)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)

numArray = NumArray([1,2,4,7,11])
# [0, 1, 3, 7, 14, 25]
print(numArray.sumRange(0,1))
numArray.update(1, 10)
print(numArray.sumRange(1,2))