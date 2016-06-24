__author__ = 'Adward'
from bintree_utils import Codec, TreeNode

class Solution(object):
    def __init__(self):
        self.cnt = 0

    def isUnivalSubtree(self, node):
        """
        :type node: TreeNode
        :rtype: int or None (
            int for True, indicating the value of this uni-value subtree;
            None for False)
        """
        leftVal = rightVal = node.val
        if node.left:
            leftVal = self.isUnivalSubtree(node.left)
        if node.right:
            rightVal = self.isUnivalSubtree(node.right)
        if node.val == leftVal and node.val == rightVal:
            self.cnt += 1
            return node.val
        else:
            return None

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.isUnivalSubtree(root)
        return self.cnt

sol = Solution()
codec = Codec()
root = codec.deserialize('{5,1,5,5,5,#,5}')
print(sol.countUnivalSubtrees(root))