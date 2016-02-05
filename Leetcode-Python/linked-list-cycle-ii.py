__author__ = 'Adward'
from time import time
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

    def buildCycle(self, lst, idx):
        head = ListNode(lst[0])
        p = head
        for value in lst[1:]:
            p.next = ListNode(value)
            p = p.next
        q = head
        for i in range(idx):
            q = q.next
        p.next = q
        return head

    def dispList(self, head):
        cnt = 0
        while head and cnt <= 10:
            print(head.val)
            head = head.next
            cnt += 1

    def reverseList(self, head):
        p1 = head
        if p1 is None:
            return None
        else:
            p2 = p1.next
            if p2 is None:
                return head
            else:
                p3 = p2.next
                p1.next = None
                p2.next = p1
                while p3:
                    p1 = p2
                    p2 = p3
                    p3 = p3.next
                    p2.next = p1
                return p2

    def copyList(self, head):
        nhead = ListNode(head.val)
        p = head.next
        q = nhead
        while p:
            print(q.next)
            if q.next:
                break
            else:
                q.next = ListNode(p.val)
            p = p.next
            q = q.next
        return nhead

    def detectCycle0(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        dict = {}
        while p:
            if p not in dict:
                dict[p] = 1
                p = p.next
            else:
                return p
        return None


    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None
        elif head.next is None:
            return None
        elif head.next == head:
            return head

        MAX_CYCLES = 100
        j = 1
        cycleLen = 1
        try:
            while True:
                p1 = head
                for i in range(MAX_CYCLES * j):
                    p1 = p1.next
                p2 = p1.next
                cycleLen = 1
                while cycleLen < MAX_CYCLES * j and p2 != p1:
                    p2 = p2.next
                    cycleLen += 1
                if cycleLen == MAX_CYCLES * j:
                    j += 1
                else:
                    break
        except AttributeError:
            return None

        left = 0
        right = MAX_CYCLES * j
        while left + 1 < right:
            mid = (left + right) // 2
            p1 = head
            for i in range(mid):
                p1 = p1.next
            p2 = p1
            for i in range(cycleLen):
                p2 = p2.next
            if p2 == p1:
                right = mid
            else:
                left = mid

        p1 = head
        for i in range(left):
            p1 = p1.next
        p2 = p1
        for i in range(cycleLen):
            p2 = p2.next
        if p2 == p1:
            return p1
        else:
            return p1.next



sol = Solution()
lst = [i for i in range(100)]
head = sol.buildCycle(lst,10)
#head = sol.buildList(lst)
result = None
t = time()
for i in range(1000):
    try:
        result = sol.detectCycle0(head).val
    except:
        result = None
print(time()-t)
print(result)
