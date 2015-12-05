__author__ = 'Adward'
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C-A) * (D-B)
        area2 = (G-E) * (H-F)
        if (E-A) * (C-G) >= 0: #include
            width = min(C-A, G-E)
        elif (A-G) * (C-E) >= 0: #separate
            width = 0
        else:
            width = min(abs(A-G), abs(C-E))

        if (F-B) * (D-H) >= 0:
            height = min(D-B, H-F)
        elif (B-H) * (D-F) >= 0:
            height = 0
        else:
            height = min(abs(B-H), abs(D-F))
        return area1 + area2 - width * height

sol = Solution()
#print(sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
#print(sol.computeArea(-3, 0, 3, 4, 3, 0, 12, 3))
#print(sol.computeArea(0,0,0,0,-1,-1,1,1))
print(sol.computeArea(-2,-2,2,2,-3,-3,3,-1))