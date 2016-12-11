__author__ = 'Adward'
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def legalMove(key1, key2):
            if key1 == 5:
                return True
            elif key1 % 2:  # corner
                return key2 % 2 == 0 or key2 == 5 or visited[(key1+key2)//2]
            else:  # side
                return key1 + key2 != 10 or visited[(key1+key2)//2]

        def backTracing(cur):
            patternCnt = 0
            if m <= len(trace) + 1 <= n:
                # legalPatterns.append(trace + [cur])
                patternCnt += 1
            if len(trace) + 1 < n:
                trace.append(cur)
                visited[cur] = True
                for dest in range(1, 10):
                    if not visited[dest] and legalMove(cur, dest):
                        patternCnt += backTracing(dest)
                visited[cur] = False
                trace.pop()
                return patternCnt
            else:
                return 1

        patternCnt = 0
        # legalPatterns = []
        trace = []
        visited = [False] * 10
        for init_key in range(1, 10):
            patternCnt += backTracing(init_key)
        return patternCnt  # , len(legalPatterns)


sol = Solution()
print(sol.numberOfPatterns(1,2))