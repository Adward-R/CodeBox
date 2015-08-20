__author__ = 'Adward'

class Solution:
    #integer[] -> unique str
    def hashingLst(self, lst):
        val = ''
        if len(lst) > 0:
            for itm in lst[::-1]:
                val += str(itm) + '.'
        return val
    # @param {integer[]} set
    # @param {integer[]} choices
    # @return {integer[][]}
    def setmultiply(self, set, choices):
        result = []
        for c in choices:
            result.append(set + [c])
        return result

    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        len_n = len(nums)
        idxs = []
        for i in range(len_n):
            idxs.append(i)
        result = [[]]
        tmp = []
        for n in idxs:
            tmp.append([n])
        result.append(tmp)

        for i in range(2, len_n+1):
            tmp = []
            for set in result[i-1]:
                for lst in self.setmultiply(set, idxs[set[-1]+1:len_n]):
                    tmp.append(lst)
            result.append(tmp)

        realResult = {}
        realResult[''] = []
        nums = sorted(nums)
        for sets in result:
            for lst in sets:
                lst = [nums[i] for i in lst]
                realResult[self.hashingLst(lst)] = lst
        return [realResult[i] for i in realResult]

sol = Solution()
print(sol.subsetsWithDup([1,2,3,4,5,6,7,8,10,0]))