class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def buildLst(self, lst):
        if len(lst) == 0:
            return None
        head = ListNode(lst[0])
        p = head
        for itm in lst[1:]:
            p.next = ListNode(itm)
            p = p.next
        return head

    def dispLst(self, head):
        p = head
        res = ''
        while p:
            res += str(p.val) + ', '
            p = p.next
        return res

    #except deleting the tail
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if (not node) or (not node.next):
            return
        p1 = node
        p2 = node.next
        while True:
            p1.val = p2.val
            if p2.next:
                p1 = p2
                p2 = p2.next
            else:
                p1.next = None
                break

sol = Solution()
head = sol.buildLst([1,2])
sol.deleteNode(head)
print(sol.dispLst(head))