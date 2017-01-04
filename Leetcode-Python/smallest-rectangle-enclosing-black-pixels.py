__author__ = 'Adward'
from bisect import *
class Solution(object):
    def minArea0(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        try:
            m, n = len(image), len(image[0])
        except:
            return 0

        leftMargin, rightMargin = n, n
        seq = [range(x, -1, -1), range(x+1, m)]
        row_limits = []
        for k in range(2):
            for i in seq[k]:
                left = bisect_left(image[i], '1')
                if left == n:
                    right = bisect_left(image[i][::-1], '1')
                    if right == n:
                        row_limits.append(i)
                        break
                    left = bisect_left(image[i], '1', hi=n-right)
                right = bisect_right(image[i][-1:left:-1], '0')
                leftMargin = min(leftMargin, left)
                rightMargin = min(rightMargin, right)
            else:
                row_limits.append(m if k else -1)
        print(row_limits, leftMargin, rightMargin)
        return (row_limits[1]-row_limits[0]-1) * (n-leftMargin-rightMargin)

    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def searchRows(lo, hi, opt):
            while lo != hi:
                mid = (lo + hi) // 2
                if ('1' in image[mid]) == opt:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        def searchColumns(lo, hi, top, bottom, opt):
            while lo != hi:
                mid = (lo + hi) // 2
                # projection
                if any(image[k][mid] == '1' for k in range(top, bottom)) == opt:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        top = searchRows(0, x, True)
        bottom = searchRows(x + 1, len(image), False)
        left = searchColumns(0, y, top, bottom, True)
        right = searchColumns(y + 1, len(image[0]), top, bottom, False)
        return (right - left) * (bottom - top)

sol = Solution()
image = [
  "0010",
  "0110",
  "0100"
]
image = ["0000000000000000000000000000000000000000000000","0000000000000000000000000000000000000100000000"]
print(sol.minArea(image, 1, 37))
