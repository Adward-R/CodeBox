__author__ = 'Adward'
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        rdmAddrs = []
        nrdmAddrs = []
        ptr = head
        #idxCnt = 0
        while ptr:
            rdmAddrs.append(ptr)
            nrdmAddrs.append(RandomListNode(ptr.label))
            #idxCnt += 1
            ptr = ptr.next
        nrdmAddrs.append(None)
        for i in range(len(nrdmAddrs)-1):
            nrdmAddrs[i].next = nrdmAddrs[i+1]
        for i in range(len(rdmAddrs)):
            try:
                idx = rdmAddrs.index(rdmAddrs[i].random)
                nrdmAddrs[i].random = nrdmAddrs[idx]
            except:
                pass
            
        return nrdmAddrs[0]
