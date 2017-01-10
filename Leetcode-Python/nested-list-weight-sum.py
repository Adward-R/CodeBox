__author__ = 'Adward'
# including -i & -ii

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def helper(nList, curDepth):
            return sum([curDepth * nInt.getInteger() if nInt.isInteger() else helper(nInt.getList(), curDepth+1)
                        for nInt in nList])
        return helper(nestedList, 1)

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        D = {}

        def getDepth(nList, curDepth):
            if curDepth not in D:
                D[curDepth] = []
            for ni in nList:
                if ni.isInteger():
                    D[curDepth].append(ni.getInteger())
                else:
                    getDepth(ni.getList(), curDepth+1)

        getDepth(nestedList, 1)
        mx = max(D)
        return sum([sum(D[depth]) * (mx + 1 - depth) for depth in D])