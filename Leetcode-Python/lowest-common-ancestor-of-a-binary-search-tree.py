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

    def getPath2Node(self, root, node, pathStk):
        if not root:
            return False
        pathStk.append(root)
        if pathStk[-1] == node:
            return True
        else:
            if self.getPath2Node(root.left, node, pathStk):
                return True
            elif self.getPath2Node(root.right, node, pathStk):
                return True
            else:
                pathStk.pop()
                return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathStk1 = []
        pathStk2 = []
        if self.getPath2Node(root, p, pathStk1) and self.getPath2Node(root, q, pathStk2):
            leng1 = len(pathStk1)
            leng2 = len(pathStk2)
            for i in range(min(leng1, leng2)):
                if pathStk1[i] != pathStk2[i]:
                    return pathStk1[i-1]
            if leng1 <= leng2:
                return pathStk1[-1]
            else:
                return pathStk2[-1]
        return None

    def lowestCommonAncestor2(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root


sol = Solution()
root = sol.binTreeBuild('{6,2,8,0,4,7,9,#,#,3,5}')
print(sol.lowestCommonAncestor(root, root.left.right, root.right.left).val)