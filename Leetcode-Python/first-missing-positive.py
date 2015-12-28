__author__ = 'Adward'
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        CACHE_LEN = 10
        cacheBase = -9
        cache = [0] * CACHE_LEN
        unfilled = 0
        while unfilled == 0:
            cacheBase += 10
            cache = [0] * CACHE_LEN
            unfilled = CACHE_LEN
            for n in nums:
                if cacheBase <= n < cacheBase+CACHE_LEN:
                    if cache[n-cacheBase] == 0:
                        cache[n-cacheBase] = 1
                        unfilled -= 1
                if unfilled == 0:
                    break
        for i in range(CACHE_LEN):
            if cache[i] == 0:
                return cacheBase+i

sol = Solution()
print(sol.firstMissingPositive([1]))