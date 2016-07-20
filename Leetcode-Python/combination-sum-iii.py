__author__ = 'Adward'

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int  # target
        :rtype: List[List[int]]
        """
        def csum(pre, k, n):
            if k == 1:
                if 0 < n < pre:
                    return [[n]]
                else:
                    return []
            else:
                lst = []
                for i in range(2, pre):
                    rlst = csum(i, k-1, n-i)
                    if len(rlst):
                        lst += [[i] + l for l in rlst]
                return lst

        return csum(10, k, n)


sol = Solution()
print(sol.combinationSum3(2, 0))

