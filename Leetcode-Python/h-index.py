__author__ = 'Adward'
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        if N < 1:
            return N
        mmax = max(citations)
        mmin = min(citations)
        nums = [0] * (mmax-mmin+1)

        for p in citations:
            nums[p-mmin] += 1
        ssum = 0
        nnums = []

        for i in range(mmax-mmin+1):
            ssum += nums[i]
            nnums.append((i+mmin, nums[i], ssum))
        #print(nnums)
        for i in range(len(nnums)-1, 0, -1):
            h = nnums[i][0]
            if N - nnums[i][2] <= h <= N - nnums[i-1][2]:
                return h
        return min(nnums[0][0], N)

sol = Solution()
citations = [4,4,0,0]
print(sol.hIndex(citations))

