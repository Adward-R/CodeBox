__author__ = 'Adward'
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        if leng == 0:
            return 0
        nOfBiggersAft = []
        for i in range(leng):
            nOfBiggersAft.append(0)
            for j in range(i+1, leng):
                if nums[j] > nums[i]:
                    nOfBiggersAft[-1] += 1
        #print(nOfBiggersAft)
        lngst1 = 1
        last = nOfBiggersAft[-1]
        lastVal = nums[-1]
        for i in range(leng-2, -1, -1):
            if nOfBiggersAft[i] > last and nums[i] < lastVal:
                last = nOfBiggersAft[i]
                lastVal = nums[i]
                lngst1 += 1
        lngst2 = 1
        last = nOfBiggersAft[0]
        for i in range(1, leng):
            if nOfBiggersAft[i] < last and nums[i] > lastVal:
                last = nOfBiggersAft[i]
                lastVal = nums[i]
                lngst2 += 1
        return max(lngst1, lngst2)

sol = Solution()
print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(sol.lengthOfLIS([18,55,66,2,3,54]))

