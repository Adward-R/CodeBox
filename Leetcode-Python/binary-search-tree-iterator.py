__author__ = 'Adward'

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def binTreeBuild(nodesLst):
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

class BSTIterator(object):
    def flatten(self, root):
        if not root:
            return []
        if root.left:
            if root.right:
                return self.flatten(root.left) + [root.val] + self.flatten(root.right)
            else:
                return self.flatten(root.left) + [root.val]
        else:
            if root.right:
                return [root.val] + self.flatten(root.right)
            else:
                return [root.val]

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.ascendList = self.flatten(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.ascendList) == 0:
            return False
        else:
            return True

    def next(self):
        """
        :rtype: int
        """
        try:
            theNext = self.ascendList[0]
        except:
            return None
        self.ascendList = self.ascendList[1:]
        return theNext

root = binTreeBuild('{6,4,8,1,5,7,9}')
it = BSTIterator(root)
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.hasNext())
print(it.next())

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())