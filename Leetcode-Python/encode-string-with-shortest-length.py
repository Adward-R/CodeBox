__author__ = 'Adward'
class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        DP = [[''] * (n+1) for _ in range(n+1)]

        for l in range(1, n+1):
            for i in range(0, n-l+1):
                j = i + l
                substr = s[i:j]
                DP[i][j] = substr  # initially DP[][] contains s[i:j]
                if l < 4:  # need not to compress
                    continue

                for k in range(i+1, j):
                    if len(DP[i][k]) + len(DP[k][j]) < len(DP[i][j]):
                        DP[i][j] = DP[i][k] + DP[k][j]

                # check if the substr itself can found repeated patterns
                ind = (substr + substr).find(substr, 1, -1)
                if ind >= 0:
                    rep = str((j-i) // ind) + '[' + DP[i][i+ind] + ']'
                    if len(DP[i][j]) > len(rep):
                        DP[i][j] = rep

        return DP[0][n]


sol = Solution()
print(sol.encode("abbbabbbcabbbabbbc"))
print(sol.encode("abbbabbbc"))