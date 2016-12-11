__author__ = 'Adward'

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        lastInd = {}
        startInd = 0
        mxLen = min(len(s), k)

        for i in range(len(s)):
            ch = s[i]
            if ch not in lastInd and len(lastInd) >= k:
                mxLen = max(mxLen, i - startInd)
                delKey = min(lastInd, key=lambda x: lastInd[x])
                startInd = lastInd[delKey] + 1
                del lastInd[delKey]
            lastInd[ch] = i
        return max(mxLen, len(s)-startInd)

sol = Solution()
s = "ecebaaacc"
print(sol.lengthOfLongestSubstringKDistinct(s, 3))