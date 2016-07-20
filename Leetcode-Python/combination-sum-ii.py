__author__ = 'Adward'

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # the following para is diff from -i ver.
        candCnt = {}
        for cand in candidates:
            if cand in candCnt:
                candCnt[cand] += 1
            else:
                candCnt[cand] = 1
        candidates = sorted(candCnt.keys(), reverse=True)
        ceilings = [candCnt[c] for c in candidates]

        combs = []
        multi = []
        dist = target
        while True:
            while len(multi) < len(candidates) and dist >= candidates[-1]:
                nextc = candidates[len(multi)]
                nextm = min(dist // nextc, ceilings[len(multi)])  # diff from -i
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
# combs = sol.combinationSum2([1,10,5], 10)
combs = sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print(combs)

