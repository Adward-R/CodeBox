__author__ = 'Adward'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deserialize(self, data):
        """
        :type data: str
        :rtype: TreeNode
        """

        lst = []
        for itm in data[1:-1].split(','):
            if itm == '#':
                lst.append(None)
            else:
                try:
                    lst.append(int(itm))
                except:
                    return None

        head = TreeNode(lst[0])
        q = [head]
        onLeft = True
        for num in lst[1:]:
            if num is not None:
                if onLeft:
                    q[0].left = TreeNode(num)
                    onLeft = False
                    q.append(q[0].left)
                else:
                    q[0].right = TreeNode(num)
                    onLeft = True
                    q.append(q[0].right)
                    q = q[1:]
            else:
                if onLeft:
                    onLeft = False
                else:
                    onLeft = True
                    q = q[1:]
        return head

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stk = [[root, False]]
        result = []
        while len(stk):
            if stk[-1][1]:
                result.append(stk[-1][0].val)
                stk.pop()
            else:
                stk[-1][1] = True
                p = stk[-1][0]
                if p.right:
                    stk.append([p.right, False])
                if p.left:
                    stk.append([p.left, False])
        return result

sol = Solution()
root = sol.deserialize('{}')
print(sol.postorderTraversal(root))