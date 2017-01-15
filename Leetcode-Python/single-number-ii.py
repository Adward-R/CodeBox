__author__ = 'Adward'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we need to implement a tree-time counter(base 3) that if a bit appears three time ,it will be zero.
        # curent  income  ouput
        # ab      c/c       ab/ab
        # 00      1/0       01/00
        # 01      1/0       10/01
        # 10      1/0       00/10
        # a = ~abc+a~b~c;
        # b = ~a~bc+~ab~c;
        a, b = 0, 0
        for c in nums:
            tmp_a = (~a & b & c) | (a & ~b & ~c)
            b = (~a & ~b & c) | (~a & b & ~c)
            a = tmp_a
        return a | b

sol = Solution()
nums = [3,1,2,3,2,2,1,1,4,3]
print(sol.singleNumber(nums))