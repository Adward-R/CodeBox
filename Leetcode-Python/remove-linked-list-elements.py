__author__ = 'Adward'

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def buildList(self, lst):
        head = ListNode(lst[0])
        p = head
        for value in lst[1:]:
            p.next = ListNode(value)
            p = p.next
        return head

    def dispList(self, head):
        disp = ''
        while head:
            disp += str(head.val)
            disp += ','
            head = head.next
        return disp

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        ptr = head
        while ptr and ptr.val == val:
            ptr = ptr.next
        if not ptr:
            return None
        nhead = ptr #lazy deletion

        ptr1 = nhead
        ptr2 = ptr1.next
        while True:
            while ptr2 and ptr2.val == val:
                ptr2 = ptr2.next
            if not ptr2:
                ptr1.next = None
                break
            ptr1.next = ptr2
            ptr1 = ptr2
            ptr2 = ptr1.next
        return nhead

sol = Solution()
head = sol.buildList([0])
nhead = sol.removeElements(head, 6)
print(sol.dispList(nhead))