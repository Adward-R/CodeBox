'''
You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
'''

class Solution(object):
    def circularArrayLoop(self, nums):  # O(n) + O(n)
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur, restore = 0, 1
        N = len(nums)
        traces = [None] * N  # storing head of the trace that the very element belongs to

        while cur < N:
            dir = nums[cur] > 0
            head = cur
            while traces[cur] < 0:  # unvisited
                # check if reverse direction
                step = nums[cur]
                if (step > 0) != dir:
                    break
                traces[cur] = head  # denote the trace head after checked it's applicable

                # check if spinning on the sample index
                nxt = (cur + step) % N
                if nxt == cur:  # never step in here again
                    traces[cur] = -1  # special note
                    break
                else:
                    cur = nxt

            if traces[cur] == head:  # re-entering the same trace, has a loop
                return True
            else:  # find next unvisited position
                while restore < N and traces[restore] is not None:
                    restore += 1
                cur, restore = restore, restore + 1

        return False

'''
If want O(n) space, use slow & fast pointers, and set visited elements along the input array to 0.
'''