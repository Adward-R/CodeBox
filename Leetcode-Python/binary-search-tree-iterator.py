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
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        p = root
        while p and p.left:
            self.stk.append(p)
            p = p.left
        self.cache = p

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        ret = self.cache.val
        if self.cache.right:
            p = self.cache.right
            while p.left:
                self.stk.append(p)
                p = p.left
            self.cache = p
        else:
            self.cache = self.stk.pop() if len(self.stk) else None
        return ret

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