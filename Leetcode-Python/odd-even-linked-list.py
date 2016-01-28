__author__ = 'Adward'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def lstConstruct(self, lst):
        if len(lst)==0:
            return []
        head = ListNode(lst[0])
        ptr = head
        for i in range(1, len(lst)):
            ptr.next = ListNode(lst[i])
            ptr = ptr.next
        return head

    def lstDisplay(self, head):
        if not head:
            print("empty")
        while head:
            print(head.val)
            head = head.next

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        else:
            oddHead = head
            if not head.next:
                 return head
            else:
                evenHead = head.next
                oPtr1 = oddHead
                ePtr1 = evenHead
                if not ePtr1.next:
                    return head
                else:
                    oPtr2 = ePtr1.next
                    ePtr2 = oPtr2.next #maybe None

        while ePtr2:
            oPtr1.next = oPtr2
            oPtr1 = oPtr2
            oPtr2 = ePtr2.next
            ePtr1.next = ePtr2
            ePtr1 = ePtr2
            if oPtr2:
                ePtr2 = oPtr2.next
            else:
                break

        if oPtr2:
            oPtr1.next = oPtr2
            oPtr2.next = evenHead
            ePtr1.next = None
        else:
            oPtr1.next = evenHead
        return head



sol = Solution()
lst = []
head = sol.lstConstruct(lst)
head = sol.oddEvenList(head)
sol.lstDisplay(head)