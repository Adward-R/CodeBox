from time import time

class Solution(object):
    def longestPalindromeSubseq0(self, s):  # bottom-up
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        dp = [[0] * N for i in range(N)]
        for i in range(N):
            dp[i][i] = 1
        for width in range(2, N + 1):
            for i in range(N):
                j = i + width - 1
                if j >= N:
                    break
                if s[i] == s[j]:  # dp[1][2] = dp[2][1] + 2 = 2, using the lower triangle to avoid index error
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][N - 1]

    def longestPalindromeSubseq(self, s):
        N = len(s)
        dp = [[0] * N for i in range(N)]
        for i in range(N):
            dp[i][i] = 1
        for i in range(N-2, -1, -1):
            for j in range(i+1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

sol = Solution()
s = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
# s = 'bbbab'
t = time()
print(sol.longestPalindromeSubseq(s))
print(time() - t)