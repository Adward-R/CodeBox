from copy import deepcopy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k < 0 or k > n:
            return []
        elif k == 0:
            return [[]]

        combs = []
        vec = [i+1 for i in range(k)]
        flag = True
        while flag: #vec[-1] <= n:
            combs.append(deepcopy(vec))
            vec[-1] += 1
            npop = 0
            while flag and vec[-1] > n - npop:
                vec.pop()
                npop += 1
                try:
                    vec[-1] += 1
                except:
                    flag = False
            if flag:
                for i in range(npop):
                    vec.append(vec[-1]+1)
        return combs

sol = Solution()
print(sol.combine(5, 2))
