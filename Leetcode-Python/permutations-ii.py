__author__ = 'Adward'
from itertools import permutations

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [list(i) for i in set(permutations(nums))]

sol = Solution()
permutes = sol.permuteUnique([1,1,2])
print(permutes)