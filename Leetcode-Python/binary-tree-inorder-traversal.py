__author__ = 'Adward'
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def binTreeBuild(self, nodesLst):
        """
        :type nodesLst: str
        :rtype: TreeNode
        """
        lst = nodesLst[1:-1].split(',')
        if (not lst[0].isdigit()) and (not lst[0][1:].isdigit()):
            return None
        head = TreeNode(int(lst[0]))
        q = [head]
        onLeft = True
        for num in lst[1:]:
            if num.isdigit() or num[1:].isdigit():
                if onLeft:
                    q[0].left = TreeNode(int(num))
                    onLeft = False
                    q.append(q[0].left)
                else:
                    q[0].right = TreeNode(int(num))
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

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stk = [root]
        preLeng = 0
        while len(stk) > 0:
            ptr = stk[-1]
            if ptr.left and len(stk) >= preLeng:
                preLeng = len(stk)
                stk.append(ptr.left)
                #ptr.left = None
            else:
                res.append(ptr.val)
                preLeng = len(stk)
                stk.pop()
                if ptr.right:
                    preLeng = len(stk)
                    stk.append(ptr.right)
        return res

sol = Solution()
root = sol.binTreeBuild('{1,#,2,3}')
print(sol.inorderTraversal(root))