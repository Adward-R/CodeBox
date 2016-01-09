__author__ = 'Adward'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums[1:]:
            nums[0] ^= n
        return nums[0]

sol = Solution()
print(sol.singleNumber([3,3,2,1,2,5,5,1,6]))