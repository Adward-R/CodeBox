__author__ = 'Adward'
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)

    def postorderTraversal(self, root):
        if root is None:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.val)

    def constructList(self, lst):
        """
        :type lst: List[int]
        :rtype: ListNode
        """
        if len(lst) == 0:
            return None
        head = ListNode(lst[0])
        ptr = head
        for v in lst[1:]:
            ptr.next = ListNode(v)
            ptr = ptr.next
        return head

    def listToBST(self, head, leng):
        """
        :type head: ListNode
        :type leng: int
        :rtype: TreeNode
        """
        if leng == 0:
            return None
        elif leng == 1:
            return TreeNode(head.val)
        else:
            mid = int(leng/2)
            ptr = head
            for i in range(mid):
                ptr = ptr.next
            root = TreeNode(ptr.val)
            root.left = self.listToBST(head, mid)
            root.right = self.listToBST(ptr.next, leng-mid-1)
            return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        leng = 0
        ptr = head
        while ptr:
            leng += 1
            ptr = ptr.next
        return self.listToBST(head, leng)

sol = Solution()
root = sol.sortedListToBST(sol.constructList([1,2,3,4,5,6,7,8]))
#root = sol.buildTree([])
sol.postorderTraversal(root)
print('===')
sol.inorderTraversal(root)

'''
1
2
4
3
6
8
7
5
===
1
2
3
4
5
6
7
8
'''