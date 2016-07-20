__author__ = 'Adward'
from copy import deepcopy

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combs = []
        candidates.sort(reverse=True)
        multi = []
        dist = target
        while True:
            while len(multi) < len(candidates) and dist >= candidates[-1]:
                nextc = candidates[len(multi)]
                nextm = dist // nextc
                dist -= nextm * nextc
                multi.append(nextm)
            if dist == 0:
                combs.append([])
                for i in range(len(multi)-1, -1, -1):
                    combs[-1] += [candidates[i]] * multi[i]
            while len(multi) and multi[-1] == 0:
                multi.pop()
            if len(multi):
                multi[-1] -= 1
                dist += candidates[len(multi)-1]
            else:
                break
        return combs

sol = Solution()
# combs = sol.combinationSum([7,3,2], 18)
combs = sol.combinationSum([1,10,5], 10)
print(combs)

