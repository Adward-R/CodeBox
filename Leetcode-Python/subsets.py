__author__ = 'Adward'

class Solution:
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
    def subsets(self, nums):
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

        realResult = [[]]
        nums = sorted(nums)
        for sets in result:
            for lst in sets:
                try:
                    realResult.append([nums[i] for i in lst])
                except:
                    print(lst)
        return realResult

sol = Solution()
print(sol.subsets([4,1,0]))
