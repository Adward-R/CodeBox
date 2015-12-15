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
        while head:
            print(head.val)
            head = head.next

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lessNodes = []
        moreNodes = []
        ptr = head
        while ptr:
            if ptr.val < x:
                lessNodes.append(ptr)
            else:
                moreNodes.append(ptr)
            ptr = ptr.next

        lessNodes += moreNodes
        leng = len(lessNodes)
        if leng == 0:
            return None
        for i in range(1, leng):
            lessNodes[i-1].next = lessNodes[i]
        lessNodes[-1].next = None
        return lessNodes[0]

    def partition1(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lessHead = None
        moreHead = None
        lessPtr = None
        morePtr = None
        ptr = head
        while ptr:
            if ptr.val < x:
                if lessHead:
                    lessPtr.next = ptr
                    lessPtr = lessPtr.next
                else:
                    lessHead = lessPtr = ptr
            else:
                if moreHead:
                    morePtr.next = ptr
                    morePtr = morePtr.next
                else:
                    moreHead = morePtr = ptr
            ptr = ptr.next
        if lessHead:
            lessPtr.next = moreHead
            if moreHead:
                morePtr.next = None
            return lessHead
        else:
            if moreHead:
                morePtr.next = None
            return moreHead

sol = Solution()
lst = sol.buildList([1,4,3,2,5,2])
sol.dispList(sol.partition1(lst, 3))