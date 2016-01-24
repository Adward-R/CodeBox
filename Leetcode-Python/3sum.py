__author__ = 'Adward'
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        threeSums = []
        n = len(nums)
        i = 0
        while i < n:
            print(i)
            target = - nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target:
                    if len(threeSums) == 0 or \
                                    nums[i] != threeSums[-1][0] or \
                                    nums[l] != threeSums[-1][1] or \
                                    nums[r] != threeSums[-1][2]:
                        threeSums.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif twoSum < target:
                    l += 1
                else:
                    r -= 1
            lasti = nums[i]
            i += 1
            while i < n and nums[i] == lasti:
                i += 1
        return threeSums

sol = Solution()
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
#nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))