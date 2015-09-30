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

    nodeList = []

    def preorderTraversal(self, root):
        if not root:
            return
        else:
            self.nodeList.append(root)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.nodeList = []
        self.preorderTraversal(root)
        self.nodeList.append(None)
        for i in range(len(self.nodeList)-1):
            self.nodeList[i].right = self.nodeList[i+1]
            self.nodeList[i].left = None

    def preorderDisplay(self, root):
        if not root:
            return
        else:
            print(root.val)
            self.preorderDisplay(root.left)
            self.preorderDisplay(root.right)

sol = Solution()
root = sol.binTreeBuild('{1,2,5,3,4,#,6}')
sol.flatten(root)
sol.preorderDisplay(root)