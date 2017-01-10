__author__ = 'Adward'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxNodes = 1

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def checkBST(root):
            valid, nNodes = True, 1
            subMinLeft = subMaxRight = root.val
            if root.left:
                _valid, subNodes, subMaxLeft, subMinLeft = checkBST(root.left)
                nNodes += subNodes
                valid &= _valid and subMaxLeft < root.val
            if root.right:
                _valid, subNodes, subMaxRight, subMinRight = checkBST(root.right)
                nNodes += subNodes
                valid &= _valid and subMinRight > root.val
            if valid:
                self.maxNodes = max(self.maxNodes, nNodes)
            return valid, nNodes, subMaxRight, subMinLeft

        if not root:
            return 0
        self.maxNodes = 1
        checkBST(root)
        maxNodes, self.maxNodes = self.maxNodes, 1
        return maxNodes