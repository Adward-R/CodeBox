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

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        headOfUnsorted = None
        nextH = head.next
        if not nextH:
            return head
        lastp = head
        lastVal = head.val
        head.next = None

        while nextH:
            headOfUnsorted = nextH
            if headOfUnsorted.val < head.val:
                after = head
                head = headOfUnsorted
            else:
                if headOfUnsorted.val > lastVal:
                    p = lastp
                    while p.next and p.next != headOfUnsorted \
                            and headOfUnsorted.val > p.next.val:
                        p = p.next
                    after = p.next
                elif headOfUnsorted == lastVal:
                    p = lastp
                    after = lastp.next
                else:
                    p = head
                    while p.next and p.next != lastp \
                            and headOfUnsorted.val > p.next.val:
                        p = p.next
                    after = p.next

            nextH = headOfUnsorted.next
            if after != headOfUnsorted:
                headOfUnsorted.next = after
                if head != headOfUnsorted:
                    p.next = headOfUnsorted
            else:
                headOfUnsorted.next = None

            lastp = headOfUnsorted
            lastVal = headOfUnsorted.val
        return head

sol = Solution()
lst = [3,4,1]
head = sol.lstConstruct(lst)
head = sol.insertionSortList(head)
sol.lstDisplay(head)