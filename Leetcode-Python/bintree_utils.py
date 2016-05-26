__author__ = 'Adward'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec(object):
    def serialize(self, head): #level-order
        """
        :type head: TreeNode
        :rtype: str
        """
        if not head:
            return '{}'
        res = []
        q = [head]
        while len(q) != 0:
            try:
                res.append(str(q[0].val))
                q.append(q[0].left)
                q.append(q[0].right)
            except:
                res.append('#')
            q = q[1:]

        while res[-1] == '#':
            res.pop()
        return '{' + ','.join(res) + '}'

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