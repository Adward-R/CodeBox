__author__ = 'Adward'
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volume = 0
        i, j = 0, len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            volume = max(volume, (j - i) * h)
            while i < j and height[i] <= h:
                i += 1
            while i < j and height[j] <= h:
                j -= 1
        return volume