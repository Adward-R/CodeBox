__author__ = 'Adward'
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        pprevMax, prevMax = nums[0], max(nums[0:2])
        for i in range(2, len(nums)):
            pprevMax, prevMax = prevMax, max(nums[i] + pprevMax, prevMax)
        return prevMax
        
sol = Solution()
nums = [7]
print(sol.rob(nums))
