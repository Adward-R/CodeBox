__author__ = 'Adward'
class Solution(object):
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) // 2
            if half == 0:
                return enum
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    # keep track of how many numbers in right part that left[-1] jumps over while conquering
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def countSmaller0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        class TNode(object):
            def __init__(self, val):
                self.val = val
                self.dup = 1
                self.left = None
                self.right = None
                self.leftSub = 0

        try:
            root = TNode(nums[-1])
        except:
            return nums
        nums[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            p = root
            val = nums[i]
            nums[i] = 0
            while True:
                if val < p.val:
                    p.leftSub += 1
                    if p.left:
                        p = p.left
                    else:
                        p.left = TNode(val)
                        break
                elif val > p.val:
                    nums[i] += p.leftSub + p.dup  # trap!!
                    if p.right:
                        p = p.right
                    else:
                        p.right = TNode(val)
                        break
                else:
                    nums[i] += p.leftSub
                    p.dup += 1
                    break
        return nums

sol = Solution()
nums = [3,4,6,2,5,1,7,3]
# nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
print(sol.countSmaller(nums))

