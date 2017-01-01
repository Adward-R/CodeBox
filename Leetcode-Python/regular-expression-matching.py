__author__ = 'Adward'
class Solution(object):
    def isMatch0(self, s, p):  # slow recursive version
        """
        :param s: str
        :param p: str
        :return: bool
        """
        if len(p) == 0:
            return len(s) == 0
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (len(s) > 0 and p[0] in (s[0], '.') and self.isMatch(s[1:], p))
        else:
            return len(s) > 0 and p[0] in (s[0], '.') and self.isMatch(s[1:], p[1:])

    def isMatch(self, s, p):  # DP version
        # DP[i][j] = isMatch(s[:i], p[:j])
        m, n = len(s)+1, len(p)+1
        DP = [[False] * n for _ in range(m)]
        # DP[x][0] = False
        DP[0][0] = True  # empty seq match empty pattern

        for j in range(2, n):
            DP[0][j] = p[j-1] == '*' and DP[0][j-2]

        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] != '*':
                    DP[i][j] = DP[i-1][j-1] and p[j-1] in (s[i-1], '.')
                else:  # matches empty seq || matches more
                    # p[0] cannot be '*' so no need to check "j > 1" here
                    DP[i][j] = DP[i][j-2] or (p[j-2] in (s[i-1], '.') and DP[i-1][j])

        return DP[-1][-1]


sol = Solution()
s = "aab"
p = "c*a*b"
print(sol.isMatch("ab", ".*c"))
print(sol.isMatch("aa", "a*"))
print(sol.isMatch(s, p))
