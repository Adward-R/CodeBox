__author__ = 'Adward'
from collections import defaultdict
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnt = 0
        # maps[i] stands for {step: nums of distinct subseq that end at i}
        maps = [defaultdict(int) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i):
                step = A[i] - A[j]
                maps[i][step] += 1
                if step in maps[j]:
                    maps[i][step] += maps[j][step]
                    cnt += maps[j][step]
        return cnt

sol = Solution()
A = [2,4,6,8,10]
A = [3, -1, -5, -9]
# A = [7,7,7,7]
print(sol.numberOfArithmeticSlices(A))
