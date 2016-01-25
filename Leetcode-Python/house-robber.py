__author__ = 'Adward'
class Solution(object):
    def rob0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            return max(nums[0] + self.rob0(nums[2:]), self.rob0(nums[1:]))

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        maxAmount = [0] * len(nums)
        maxAmount[0] = nums[0]
        maxAmount[1] = max(nums[0:2])
        for i in range(2, len(nums)):
            maxAmount[i] = max(nums[i] + maxAmount[i-2], maxAmount[i-1])
        return maxAmount[-1]


sol = Solution()
nums = [7]
print(sol.rob(nums))
