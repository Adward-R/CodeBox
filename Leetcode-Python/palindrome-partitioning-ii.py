__author__ = 'Adward'

class Solution(object):
    def minCut(self, s):
        N = len(s)
        table = [[False] * N for _ in range(N)]
        for i in range(N):
            table[i][i] = True
        for i in range(N-1):
            table[i][i+1] = s[i] == s[i+1]
        for l in range(2, N):
            for i in range(N-l):
                j = i + l
                table[i][j] = table[i+1][j-1] and s[i] == s[j]

        dp = [N] * N  # dp[i] stands for minimum cut in s[0:i+1]
        dp[0] = 0

        for i in range(N):
            for j in range(i, N):
                if table[i][j]:
                    dp[j] = min(dp[j], dp[i-1] + 1) if i > 0 else 0
        return dp[-1]


sol = Solution()
s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
s = "ababababababababababababcbabababababababababababa"
print(sol.minCut(s))