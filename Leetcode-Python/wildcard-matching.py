__author__ = 'Adward'
class Solution(object):
    def isMatch0(self, s, p):  # DP version
        # DP[i][j] = isMatch(s[:i], p[:j])
        m, n = len(s)+1, len(p)+1
        DP = [[False] * n for _ in range(m)]
        # DP[x][0] = False
        DP[0][0] = True  # empty seq match empty pattern
        for j in range(1, n):
            DP[0][j] = p[j-1] == '*' and DP[0][j-1]

        pmatched = [_ for _ in DP[0]]  # record if p[:j] has ever matched any prev str

        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] != '*':
                    DP[i][j] = DP[i-1][j-1] and p[j-1] in (s[i-1], '?')
                else:
                    DP[i][j] = pmatched[j-1]
                    # k = i
                    # while k >= 0 and not DP[k][j-1]:
                    #     k -= 1
                    # DP[i][j] = k >= 0
                if not pmatched[j] and DP[i][j]:
                    pmatched[j] = True

        return DP[-1][-1]

    def isMatch(self, s, p):  # O(N) ver.
        # DP[i][j] = isMatch(s[:i], p[:j])
        i, j, match, i_star = 0, 0, 0, -1
        while i < len(s):
            # advancing both pointers
            if j < len(p) and p[j] in (s[i], '?'):
                i, j = i+1, j+1
            # '*' found, only advancing pattern ptr
            elif j < len(p) and p[j] == '*':
                i_star = j
                match = i
                j += 1
            # last j points to a '*' in pattern, advancing str ptr
            elif i_star != -1:
                j = i_star + 1
                match += 1
                i = match
            else:
                return False

        # check remaining patterns
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

sol = Solution()
print(sol.isMatch("aa", "a"))
print(sol.isMatch("aa", "aa"))
print(sol.isMatch("aaa", "aa"))
print(sol.isMatch("aa", "*"))
print(sol.isMatch("aa", "a*"))
print(sol.isMatch("ab", "?*"))
print(sol.isMatch("aab", "c*a*b"))
s = "baabbabaaaabababbbabbaabbabbabbbbbbabaaaaababbbaababaaabaaaabbbaaaaaaaaaabbaaaaaaabaabbabaaabaaaaaabaabbbabbbbbbaabababbabbabaaaaabbaaabbbaaabbababaaabbbbbbbbbbbaabaaabbababaaaababbaabbbaaabbbbaabaaba"
p = "a*a*b*bb*ba***aab***b******aabaa*a*a*a*b**abbb***a*b*a*a*bb**ba****baa*****a*b***aaab*bab*****bb*a**"
print(sol.isMatch(s, p))
