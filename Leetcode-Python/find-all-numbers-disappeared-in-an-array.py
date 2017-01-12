__author__ = 'Adward'
class Solution(object):  # Two Solutions
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            val = abs(i) - 1
            if nums[val] > 0:
                nums[val] = - nums[val]

        return [ind + 1 for ind in range(len(nums)) if nums[ind] > 0]

    def findDisappearedNumbers1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1] and nums[i] != i + 1:  # swap with numbers on its right
                tmp = nums[i]
                nums[i], nums[tmp-1] = nums[tmp-1], nums[i]
        return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]

sol = Solution()
for nums in [
    [4,3,2,7,8,2,3,1],
    [2,5,3,6,1,4]
]:
    print(sol.findDisappearedNumbers(nums))