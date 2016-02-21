__author__ = 'Adward'
from random import random
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        i = 0
        while i < len(nums) - 1 and nums[i] >= nums[i+1]:
            i += 1
        if i == len(nums) - 1:
            return False
        else:
            cache = [nums[i], nums[i+1]]

        i += 2
        scache = None

        while i < len(nums):
            ni = nums[i]
            if ni > cache[1]:
                return True
            else:
                if scache:
                    if ni > scache:
                        if cache[1] > ni:
                            cache = [scache, ni]
                            scache = None
                    else:
                        scache = ni
                else:
                    if ni > cache[0]:
                        cache[1] = ni
                    elif ni < cache[0]:
                        scache = ni
            i += 1
        return False


def randSeqGen(max_len):
    leng = int(random() * (max_len-3) + 1) + 3
    return [int(random() * max_len) for i in range(leng)]

sol = Solution()
#nums = [5,4,3,2,1]
#nums = [1,5,2,4,3]
#nums = [7,5,6,3,4,1,2]
#nums = [7,1,6,2,5,3]
#nums = randSeqGen(7)
#print(nums)
nums = []
print(sol.increasingTriplet(nums))