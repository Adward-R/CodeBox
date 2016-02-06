__author__ = 'Adward'
class Solution(object):
    def jump0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        minJumps = len(nums)
        path = [0]
        while True:
            #print(path)
            flag = False
            if nums[path[-1]] != 0:
                path.append(path[-1] + nums[path[-1]])
            else:
                flag = True
            if len(path) >= minJumps:
                flag = True
            if path[-1] >= len(nums)-1:
                flag = True
                if len(path) < minJumps:
                    minJumps = len(path)
                path.pop()

            if flag:
                path[-1] -= 1
                while len(path) >= 2 and path[-1] == path[-2]:
                    path.pop()
                    path[-1] -= 1
                if len(path) < 2:
                    break
        return minJumps-1

    def jump1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        elif len(nums) > 1000:
            return self.jump0(nums)
        stepMatrix = [[len(nums)]*len(nums) for i in range(len(nums))]
        rowPtrs = [0] * len(nums) #automatically ignore '0'
        for i in range(len(nums)-1):
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                stepMatrix[i][j] = 1
                rowPtrs[i] = i+nums[i]+1

        for i in range(len(nums)-3, -1, -1):
            for j in range(i+1, rowPtrs[i]):
                for k in range(j+1, len(nums)):
                    stepMatrix[i][k] = min(stepMatrix[i][k], stepMatrix[j][k]+1)

        #for row in stepMatrix:
        #    print(row)
        return stepMatrix[0][-1]

    def jump(self, nums):
        near, far, step = 0, 1, 0
        while far < len(nums):
            nfar = max( i + j for i, j in zip( range(near, far), nums[near:far] ) ) + 1
            near, far, step = far, nfar, step + 1
        return step


sol = Solution()
#nums = [3,2,0,4,1,1,2,3,0,1,1,2]
#nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
nums = [1] * 25000
nums = [i for i in range(25000, 0, -1)] + [1, 0]
print(sol.jump(nums))