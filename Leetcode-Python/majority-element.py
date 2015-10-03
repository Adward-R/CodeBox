__author__ = 'Adward'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        possible = {}
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1] \
                    and nums[i] not in possible.keys():
                possible[nums[i]] = 0
        for i in range(n):
            if nums[i] in possible.keys():
                possible[nums[i]] += 1

        try:
            majorVal = max(possible.values())
        except: # n is odd, like 10101
            return nums[0]
        for key in possible.keys():
            if possible[key] == majorVal:
                return key


sol = Solution()
print(sol.majorityElement([1,0,1,0,1]))