__author__ = 'Adward'

class NumArray(object):
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


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

numArray = NumArray([1,2,4,7,11])
print(numArray.sumRange(3,4))