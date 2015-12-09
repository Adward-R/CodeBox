__author__ = 'Adward'
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hasZero = False
        nnums = [[]]
        for n in nums:
            if n:
                nnums[-1].append(n)
            else:
                hasZero = True
                if len(nnums[-1]):
                    nnums.append([])
        if len(nnums[-1]) == 0:
            del nnums[-1]

        mmax = - 1 << 31
        for nums in nnums:
            mul = 1
            posMul = [1]
            negMul = []
            for n in nums:
                mul *= n
                if mul > 0:
                    posMul.append(mul)
                else:
                    negMul.append(mul)
            #print(posMul)
            #print(negMul)
            if len(posMul) == 1:
                if len(negMul) == 1:
                    mmax = max(negMul[0], mmax)
                else:
                    mmax = max(negMul[-1]/negMul[0], mmax)
            elif len(negMul) == 0:
                mmax = max(posMul[-1]/posMul[0], mmax)
            else:
                mmax = max(posMul[-1]/posMul[0], negMul[-1]/negMul[0], mmax)

        if hasZero:
            return max(int(mmax), 0)
        else:
            return int(mmax)

sol = Solution()
print(sol.maxProduct([5,-2,-5,1,2,-2,3,0,0,2]))
print(sol.maxProduct([-2]))
print(sol.maxProduct([0,0,0,-1,-2]))