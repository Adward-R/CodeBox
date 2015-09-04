__author__ = 'Adward'

'''
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        try:
            distTriangle = [triangle[0]]
        except:
            return 0
        for i in range(1, len(triangle)):
            distTriangle.append([])
            for j in range(i+1):
                if j == 0:
                    distTriangle[i].append(distTriangle[i-1][0] + triangle[i][j])
                elif j == i:
                    distTriangle[i].append(distTriangle[i-1][i-1] + triangle[i][j])
                else:
                    distTriangle[i].append(min(distTriangle[i-1][j-1], distTriangle[i-1][j]) + triangle[i][j])
        #print(distTriangle)
        return min(distTriangle[-1])

sol = Solution()
'''
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
'''
triangle = [
    [2]
]
print(sol.minimumTotal(triangle))