__author__ = 'Adward'
# import copy
class Solution(object):
    # def singleNumber2(self, nums): # slow!
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     hashTbl = [None] * 17
    #     validNum = 0
    #     storage = copy.deepcopy(nums)
    #     cache = []
    #
    #     while True:
    #         for i in storage:
    #             idx = i % 17
    #             if hashTbl[idx] is None:
    #                 hashTbl[idx] = i
    #                 validNum += 1
    #             else:
    #                 if hashTbl[idx] == i:
    #                     hashTbl[idx] = None
    #                     validNum -= 1
    #                 else:
    #                     cache.append(hashTbl[idx])
    #                     hashTbl[idx] = i
    #
    #         if validNum == 2 and len(cache) == 0:
    #             res = []
    #             for i in hashTbl:
    #                 if i:
    #                     res.append(i)
    #             return res
    #         elif validNum == 1 and len(cache) == 1:
    #             res = []
    #             for i in hashTbl:
    #                 if i:
    #                     res.append(i)
    #             res.append(cache[0])
    #             return res
    #         elif validNum == 0 and len(cache) == 2:
    #             return cache
    #         else:
    #             storage = []
    #             storage = copy.deepcopy(cache)
    #             cache = []

    def singleNumber(self, nums):
        diff = nums[0]
        # Get the XOR of the two numbers we need to find
        for num in nums[1:]:
            diff ^= num
        # Get its last set bit
        diff &= - diff
        rets = [0] * 2
        # If the bit is set, belongs to one of the remaining return number
        # else belongs to another
        for num in nums:
            rets[int(not (num & diff))] ^= num
        return rets

sol = Solution()
print(sol.singleNumber([1403617094,-490450406,-1756388866,-967931676,1878401007,1878401007,-74743538,1403617094,-1756388866,-74743538,-490450406,-1895772685]))
#print(1^1^2^2^3^4)
