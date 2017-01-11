__author__ = 'Adward'
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low) > 0:
            return max(self.strobogrammaticInRange('0', high)
                       - self.strobogrammaticInRange('0', str(int(low)-1)), 0)

        candidates = (0, 1, 6, 8, 9)

        nsums = [3, 4]
        LH, IH = len(high), int(high)
        if LH == 1:
            return 3 if IH >= 8 else (2 if IH >= 1 else 1)
        for L in range(3, LH):
            nsums.append(nsums[-1] * 3 if L % 2 else nsums[-1] * 5 // 3)
        nsum = sum(nsums) if LH > 2 else (3 if LH == 2 else 0)

        half, isOdd = LH // 2, LH % 2
        for i in range(half):
            digit = int(high[i])
            j = 0 if i else 1  # i == 0 : boundary digit selection
            while j < 5 and candidates[j] < digit:
                j += 1
            nsum += (j - (0 if i else 1)) * (5 ** (half - 1 - i)) * (3 if isOdd else 1)
            if j < 5 and candidates[j] > digit:
                return nsum

        if isOdd:
            pivots = (0, 1, 8)
            mid = int(high[half])
            nsum += len([d for d in pivots if d < mid])
            if mid not in pivots:
                return nsum
        # if mirror of first half < second half of 'high', then nsum += 1
        for i in range(half):
            j = LH - 1 - i
            digit = int(high[i])
            mirror = 6 if digit == 9 else (9 if digit == 6 else digit)
            if mirror > int(high[j]):
                break
        else:
            nsum += 1

        return nsum

sol = Solution()
# print(sol.strobogrammaticInRange('50', '100'))
# print(sol.strobogrammaticInRange('1', '1'))
# print(sol.strobogrammaticInRange('1001', '11111'))
print(sol.strobogrammaticInRange('10000001', '20000000'))