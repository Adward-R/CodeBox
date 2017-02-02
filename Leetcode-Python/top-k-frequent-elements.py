from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cntr = Counter(nums)
        buckets = []
        for num in cntr:
            if cntr[num] > len(buckets):
                buckets += [[] for _ in range(cntr[num]-len(buckets)-1)]
                buckets.append([num])
            else:
                buckets[cntr[num]-1].append(num)
        topk = []
        for buc in buckets[::-1]:
            topk += buc
            if len(topk) >= k:
                return topk[:k]

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))