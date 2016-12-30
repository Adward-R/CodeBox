__author__ = 'Adward'
from itertools import combinations
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1  # first num we cannot reach, meaning [1,miss) can all be constructed now
        patched, i = 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2  # patch miss itself to array, (double) extend the range
                patched += 1
        return patched

sol = Solution()
# nums = [2,2,4,16,21,28,33,43,44,45,48,59,70,70,73,73,74,78,83,85,88,96,96,100]
# print(sol.minPatches(nums, 56))
nums = [1, 2, 31, 33]
print(sol.minPatches(nums, 2147483647))