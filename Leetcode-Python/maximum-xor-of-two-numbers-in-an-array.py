__author__ = 'Adward'
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(format(max(nums), 'b'))-1, -1, -1):
            ans <<= 1
            prefixes = {num >> i for num in nums}
            ans += any(ans ^ 1 ^ p in prefixes for p in prefixes)
        return ans
        # maxNum = max(nums)
        # maxBits = format(maxNum, 'b')
        # N = len(maxBits)
        # bits = [[[], []] for _ in range(N)]
        # for num in nums:
        #     # if num == maxNum:
        #     #     continue
        #     tmp = num
        #     ind = 0
        #     while tmp:
        #         bits[ind][tmp % 2].append(num)
        #         tmp //= 2
        #         ind += 1
        #
        # ans = 0
        # for n1 in bits[-1][1]:
        #     n1Bits = [int(ch) for ch in format(n1, 'b')]
        #     pool = set()
        #     for pwr in range(N-2, -1, -1):
        #         cands = bits[pwr][not n1Bits[N-1-pwr]]
        #         if len(cands):
        #             if len(pool):
        #                 pool.intersection(cands)
        #             else:
        #                 pool.update(cands)
        #     ans = max(ans, n1 )

sol = Solution()
nums = [3, 10, 5, 25, 2, 8]
print(sol.findMaximumXOR(nums))