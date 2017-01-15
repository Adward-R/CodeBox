__author__ = 'Adward'
from heapq import *
from collections import defaultdict
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if k < 2:
            return [d * 1.0 for d in nums]
        smaller, larger = [], []  # max-heap & min-heap, len(smaller) <= len(larger)
        lazy_del = defaultdict(int)

        for i in range(k):
            heappush(larger, nums[i])
        for _ in range(k//2):
            heappush(smaller, -heappop(larger))

        medians = []
        for i in range(k, len(nums)+1):
            medians.append(larger[0] * 1.0 if k % 2 else (larger[0] - smaller[0]) / 2.0)
            if i == len(nums):
                break
            balance = 0
            # what happens to the num moving out
            out = nums[i-k]
            if out <= -smaller[0]:
                balance += 1
                if out == -smaller[0]:
                    heappop(smaller)
                else:
                    lazy_del[out] += 1
            else:
                balance -= 1
                if out == larger[0]:
                    heappop(larger)
                else:
                    lazy_del[out] += 1

            # push the new number to heap
            if len(larger) == 0 or nums[i] >= larger[0]:
                heappush(larger, nums[i])
                balance += 1
            else:
                heappush(smaller, -nums[i])
                balance -= 1

            # re-balance
            if balance > 0:
                heappush(smaller, -heappop(larger))
            elif balance < 0:
                heappush(larger, -heappop(smaller))

            # perform lazy deletion on top of each heap
            while len(smaller) and -smaller[0] in lazy_del and lazy_del[-smaller[0]] > 0:
                lazy_del[-heappop(smaller)] -= 1
            while len(larger) and larger[0] in lazy_del and lazy_del[larger[0]] > 0:
                lazy_del[heappop(larger)] -= 1

        return medians

sol = Solution()
nums = [
    [1,3,-1,-3,5,3,6,7],
    [-2147483648,-2147483648,2147483647,-2147483648,-2147483648,-2147483648,2147483647,2147483647,2147483647,2147483647,-2147483648,2147483647,-2147483648],
    [7,9,3,8,0,2,4,8,3,9],
    [4,1,7,1,8,7,8,7,7,4],
    [1,4,2,3]
]
sizes = [3, 2, 1, 4, 4]
for ind in range(5):
    print(sol.medianSlidingWindow(nums[ind], sizes[ind]))

