__author__ = 'Adward'
from bintree_utils import Codec, TreeNode

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        p1 = root
        if p1:
            p2 = root.left
        else:
            return root

        next_left = p1.right
        while p2:
            next_p2 = p2.left
            p2.left = next_left
            next_left = p2.right
            p2.right = p1
            if p1 == root:
                p1.left = p1.right = None
            p1 = p2
            p2 = next_p2
        return p1

if __name__ == '__main__':
    data = '{1,2,3,4,5,#,#,6}'
    codec = Codec()
    root = codec.deserialize(data)
    sol = Solution()
    print(codec.serialize(sol.upsideDownBinaryTree(root)))