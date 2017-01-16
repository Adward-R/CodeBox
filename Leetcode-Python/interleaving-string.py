__author__ = 'Adward'
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        elif m == 0:
            return s2 == s3
        elif n == 0:
            return s1 == s3
        # dp[i][j] means if s3[:i+j] is the interleaving of s1[:i] and s2[:j]
        dp = [[False] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[-1][-1]

sol = Solution()
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))