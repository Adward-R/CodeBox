__author__ = 'Adward'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        ans = str(root.val)
        if root.left:
            ans += ',' + self.serialize(root.left)
        if root.right:
            ans += ',' + self.serialize(root.right)
        return ans


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        data = [int(d) for d in data.split(',')]

        def helper(lo, hi, i):
            if i >= len(data):
                return None, i
            v = data[i]
            if v <= lo or v >= hi:
                return None, i
            root = TreeNode(v)
            root.left, i = helper(lo, v, i+1)
            root.right, i = helper(v, hi, i)
            return root, i

        return helper(-2**31, 2**31-1, 0)[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))