__author__ = 'Adward'
from collections import Counter
class Solution(object):
    def removeDuplicateLetters_fast(self, s):
        rindex = {c: i for i, c in enumerate(s)}  # last appearance
        result = []
        for i, c in enumerate(s):
            if c not in result:
                while result and c < result[-1] and i < rindex[result[-1]]:
                    result.pop()
                result.append(c)
        return ''.join(result)

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cntr = Counter(s)
        pos = 0  # position of the smallest s[i]
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            cntr[s[i]] -= 1
            if cntr[s[i]] == 0:  # right side doesn't have all unique characters
                break
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], "")) if len(s) else ""

sol = Solution()
#print(sol.removeDuplicateLetters('cbacdcbc'))
# print(sol.removeDuplicateLetters_fast("caccabad"))
print(sol.removeDuplicateLetters_fast("bcabc"))