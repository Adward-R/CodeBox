__author__ = 'Adward'

class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) < 2:
            return 1
        candies = [None] * len(ratings)
        i = 0
        while i < len(ratings) - 1:
            if ratings[i] > ratings[i+1]:
                j = i
                try:
                    while ratings[j] > ratings[j+1]:
                        j += 1
                except:
                    pass
                for k in range(j-i):
                    candies[j-k] = k + 1
                tmp = j - i + 1
                if candies[i] is not None:
                    if candies[i] < tmp:
                        candies[i] = tmp
                else:
                    candies[i] = tmp
                i = j

            elif ratings[i] == ratings[i+1]:
                j = i + 1
                try:
                    while ratings[j] == ratings[j+1]:
                        j += 1
                except:
                    if j+1 == len(ratings):
                        j += 1
                for k in range(i+1, j):
                    candies[k] = 1
                if i == 0:
                    candies[0] = 1
                i = j

            else:
                j = i + 1
                try:
                    while ratings[j] < ratings[j+1]:
                        j += 1
                except:
                    pass
                for k in range(i, j+1):
                    candies[k] = k - i + 1
                i = j
        #print(candies)
        return sum(candies)

sol = Solution()
print(sol.candy([1,2,3,4,5,3,2,1]))
