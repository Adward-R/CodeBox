__author__ = 'Adward'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans, q = [], []
        parents, childs = {}, {}

        def parse(node):
            subs = list(filter(lambda x: x is not None, (node.left, node.right)))
            if len(subs) == 0:
                q.append(node)
            else:
                for subnode in subs:
                    parents[subnode] = node
                    parse(subnode)
                childs[node] = len(subs)

        parse(root)
        parents[root] = None

        while len(q):
            layer, new_q = [], []
            for node in q:
                layer.append(node.val)
                parent = parents[node]
                if parent:  # not root
                    if childs[parent] == 1:
                        new_q.append(parent)
                    else:
                        childs[parent] -= 1
            ans.append(layer)
            q = new_q
        return ans