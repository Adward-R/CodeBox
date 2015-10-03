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

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        if not root:
            return view
        q = [(root, 0)]
        rightMostNode = root
        node = None
        level = 0

        while len(q) > 0:
            nnode, nlevel = q[0]
            if nlevel > level:
                view.append(node.val)
                level = nlevel
            if nnode.left:
                q.append((nnode.left, nlevel+1))
            if nnode.right:
                q.append((nnode.right, nlevel+1))
            node = nnode
            q = q[1:]

        view.append(node.val)
        return view

sol = Solution()
root = sol.binTreeBuild('{1,2,3,#,5}')
print(sol.rightSideView(root))