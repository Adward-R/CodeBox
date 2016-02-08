__author__ = 'Adward'
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder[0] == '#':
            if len(preorder) == 1:
                return True
            else:
                return False
        nodeStk = []
        nodesLst = preorder.split(',')
        i = 0
        while i < len(nodesLst):
            if nodesLst[i] == '#':
                try:
                    while not nodeStk[-1]:
                        nodeStk.pop()
                    nodeStk[-1] = False
                except:
                    if i == len(nodesLst)-1:
                        return True
                    else:
                        return False
            else:
                nodeStk.append(True)
            i += 1

        return False

sol = Solution()
preorder = "1,#,#,1"
print(sol.isValidSerialization(preorder))