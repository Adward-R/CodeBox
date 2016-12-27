__author__ = 'Adward'
import re
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        m = len(target)
        diffs = {sum(2**i for i, c in enumerate(word) if target[i] != c)
                 for word in dictionary if len(word) == m}
        if not diffs:
            return str(m)
        bits = max((i for i in range(2**m) if all(d & i for d in diffs)),
                   key=lambda bts: sum((bts >> i) & 3 == 0 for i in range(m-1)))
        s = ''.join(target[i] if bits & 2**i else '#' for i in range(m))
        return re.sub('#+', lambda x: str(len(x.group())), s)

sol = Solution()
print(sol.minAbbreviation("usaandchinaarefriends", []))