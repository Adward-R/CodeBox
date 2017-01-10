__author__ = 'Adward'
class Solution(object):
    def maximumGap(self, nums):  # nums are [0, 2^31)
        """
        :type nums: List[int]
        :rtype: int
        """
        N_BKT = 10
        if len(nums) < 2:
            return 0
        mx, mn = max(nums), min(nums)
        if mx == mn:
            return 0
        buc_size = (mx - mn) // N_BKT + 1
        buckets = [None] * N_BKT
        for num in nums:
            ind = (num - mn) // buc_size
            if buckets[ind]:
                buckets[ind]['in'].append(num)
                buckets[ind]['lo'] = min(buckets[ind]['lo'], num)
                buckets[ind]['hi'] = max(buckets[ind]['hi'], num)
            else:
                buckets[ind] = {'lo': num, 'hi': num, 'in': [num]}
        mxGap, i = 1, 0
        while i+1 < len(buckets):
            j = i + 1
            while j < N_BKT and not buckets[j]:
                j += 1
            if j < N_BKT:
                mxGap = max(mxGap, buckets[j]['lo'] - buckets[i]['hi'])
                i = j
            else:
                break
        if mxGap >= buc_size:
            return mxGap
        else:
            pool = [mxGap]
            for sub in filter(lambda x: buckets[x] and buckets[x]['hi'] - buckets[x]['lo'] > mxGap, range(N_BKT)):
                pool.append(self.maximumGap(buckets[sub]['in']))
            return max(pool)

sol = Solution()
for nums in [
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    [1, 10000000],
    [1,1,1,1],
    [1,7,7,7,7],
    [23909,19622,13107,10834,11667,28450,30959,7877,6015,4816,17362,3482,2247,230,16899,3818,4461,16494,31033,290,1918,15188,10109,30387,3570,14782,8496,11275,724,10139,20559,6597,6307,22655,14582,30492,7927,15790,10019,16550,15975,17015,27069,5951,11179,17091,16085,2882,5630,20461,21803,10240,21702,14292,1780,21354,6263,559,12762,22033,8885,22561,20549,8017,18873,2574,14297,6600,19189,10156,8512,9229,12539,24157,23849,415,20635,4540,23184,22556,8523]
]:
    print(sol.maximumGap(nums))