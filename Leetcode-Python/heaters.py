__author__ = 'Adward'
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        j = r = 0  # max-of-min problem
        H = len(heaters)
        houses.sort()
        heaters.sort()
        maxDist = 10 ** 9
        for i in range(len(houses)):
            while j < H and houses[i] > heaters[j]:
                j += 1
            r = max(r, min(heaters[j] - houses[i] if j < H else maxDist, houses[i] - heaters[j-1] if j > 0 else maxDist))
        return r

houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
sol = Solution()
print(sol.findRadius(houses, heaters))