__author__ = 'Adward'
class MedianFinder:
    class TreeNode(object):
        def __init__(self, num):
            self.num = num
            self.mmid = 1
            self.lleft = 0
            self.rright = 0
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 0
        self.tree = None

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.N += 1
        if not self.tree:
            self.tree = self.TreeNode(num)
        else:
            p = self.tree
            while p:
                pnum = p.num
                if num == pnum:
                    p.mmid += 1
                    return
                elif num < pnum:
                    p.lleft += 1
                    if not p.left:
                        p.left = self.TreeNode(num)
                        return
                    p = p.left
                else:
                    p.rright += 1
                    if not p.right:
                        p.right = self.TreeNode(num)
                        return
                    p = p.right

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.N == 0:
            return 0
        mid = (self.N - 1) // 2
        p = self.tree
        base = 0
        firstNum = None

        while p:
            num = p.num
            if base + p.lleft - 1 >= mid:
                p = p.left
            elif base + p.lleft + p.mmid - 1 >= mid:
                if firstNum is not None:
                    return float(firstNum + num) / 2
                if self.N % 2 or base + p.lleft + p.mmid - 1 > mid:
                    return float(num)
                else:
                    if not p.right:
                        mid += 1
                        p = self.tree
                        base = 0
                        firstNum = num
                    else:
                        p = p.right
                        lp = p.left
                        while lp:
                            p = lp
                            lp = p.left
                        nnum = p.num
                        return float(num + nnum) / 2
            else:
                base += p.lleft + p.mmid
                p = p.right
        return 0


# Your MedianFinder object will be instantiated and called as such:

mf = MedianFinder()
mf.addNum(6)
print(mf.findMedian())
mf.addNum(10)
print(mf.findMedian())
mf.addNum(2)
print(mf.findMedian())
mf.addNum(6)
print(mf.findMedian())
mf.addNum(5)
print(mf.findMedian())

mf.addNum(0)
print(mf.findMedian())
mf.addNum(6)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
mf.addNum(1)
print(mf.findMedian())
mf.addNum(0)
print(mf.findMedian())
mf.addNum(0)
print(mf.findMedian())
'''
mf.addNum(155),\
mf.findMedian(),mf.addNum(66),mf.findMedian(),mf.addNum(114),mf.findMedian(),mf.addNum(0),mf.findMedian(),mf.addNum(60),mf.findMedian(),mf.addNum(73),mf.findMedian(),mf.addNum(109),mf.findMedian(),mf.addNum(26),mf.findMedian(),mf.addNum(154),mf.findMedian(),mf.addNum(0),mf.findMedian(),mf.addNum(107),mf.findMedian(),mf.addNum(75),mf.findMedian(),mf.addNum(9)
mf.findMedian(),mf.addNum(57),mf.findMedian(),mf.addNum(53),mf.findMedian(),mf.addNum(6),mf.findMedian(),mf.addNum(85),mf.findMedian(),mf.addNum(151),mf.findMedian(),mf.addNum(12),mf.findMedian(),mf.addNum(110),mf.findMedian(),mf.addNum(64),mf.findMedian(),mf.addNum(103),mf.findMedian(),mf.addNum(42),mf.findMedian(),mf.addNum(103),mf.findMedian(),mf.addNum(126),mf.findMedian(),mf.addNum(3),mf.findMedian(),mf.addNum(88),mf.findMedian(),mf.addNum(142),mf.findMedian(),mf.addNum(79),mf.findMedian(),mf.addNum(88),mf.findMedian(),mf.addNum(147),mf.findMedian(),mf.addNum(47),mf.findMedian(),mf.addNum(134),mf.findMedian(),mf.addNum(27),mf.findMedian(),mf.addNum(82),mf.findMedian(),mf.addNum(95),mf.findMedian(),mf.addNum(26),mf.findMedian(),mf.addNum(124),mf.findMedian(),mf.addNum(71),mf.findMedian(),mf.addNum(79),mf.findMedian(),mf.addNum(130),mf.findMedian(),mf.addNum(91),mf.findMedian(),mf.addNum(131),mf.findMedian(),mf.addNum(67),mf.findMedian(),mf.addNum(64),mf.findMedian(),mf.addNum(16),mf.findMedian(),mf.addNum(60),mf.findMedian(),mf.addNum(156),mf.findMedian(),mf.addNum(9),mf.findMedian(),mf.addNum(65),mf.findMedian(),mf.addNum(21),mf.findMedian(),mf.addNum(66),mf.findMedian(),mf.addNum(49),mf.findMedian(),mf.addNum(108),mf.findMedian(),mf.addNum(80),mf.findMedian(),mf.addNum(17),mf.findMedian(),mf.addNum(159),mf.findMedian(),mf.addNum(24),mf.findMedian(),mf.addNum(90),mf.findMedian(),mf.addNum(79),mf.findMedian(),mf.addNum(31),mf.findMedian(),mf.addNum(79),mf.findMedian(),mf.addNum(113),mf.findMedian(),mf.addNum(39),mf.findMedian(),mf.addNum(54),mf.findMedian(),mf.addNum(156),mf.findMedian(),mf.addNum(139),mf.findMedian(),mf.addNum(8),mf.findMedian(),mf.addNum(90),mf.findMedian(),mf.addNum(19),mf.findMedian(),mf.addNum(10),mf.findMedian(),mf.addNum(50),mf.findMedian(),mf.addNum(89),mf.findMedian(),mf.addNum(77),mf.findMedian(),mf.addNum(83),mf.findMedian(),mf.addNum(13),mf.findMedian(),mf.addNum(3),mf.findMedian(),mf.addNum(71),mf.findMedian(),mf.addNum(52),mf.findMedian(),mf.addNum(21),mf.findMedian(),\
mf.addNum(50),mf.findMedian(),mf.addNum(120),mf.findMedian(),mf.addNum(159),mf.findMedian(),mf.addNum(45),mf.findMedian(),mf.addNum(22),mf.findMedian(),mf.addNum(69),mf.findMedian(),mf.addNum(144),\
mf.findMedian(),mf.addNum(158),mf.findMedian(),mf.addNum(19),mf.findMedian(),mf.addNum(109),mf.findMedian(),mf.addNum(52),mf.findMedian(),mf.addNum(50),mf.findMedian(),mf.addNum(51),mf.findMedian(),\
mf.addNum(62)
mf.findMedian()
mf.addNum(20),mf.findMedian(),mf.addNum(22),\
mf.findMedian(),mf.addNum(71),mf.findMedian(),mf.addNum(95),mf.findMedian(),\
mf.addNum(47),mf.findMedian(),mf.addNum(12),mf.findMedian(),mf.addNum(21),\
mf.findMedian(),mf.addNum(32),mf.findMedian(),mf.addNum(17),mf.findMedian(),\
mf.addNum(130),mf.findMedian(),mf.addNum(109),mf.findMedian(),\
mf.addNum(8),mf.findMedian(),mf.addNum(61),mf.findMedian(),mf.addNum(13),mf.findMedian(),mf.addNum(48),mf.findMedian(),mf.addNum(107),mf.findMedian(),mf.addNum(14),mf.findMedian(),mf.addNum(122),mf.findMedian(),mf.addNum(62),mf.findMedian(),mf.addNum(54),mf.findMedian(),mf.addNum(70),mf.findMedian(),mf.addNum(96),mf.findMedian(),mf.addNum(11),mf.findMedian(),mf.addNum(141),mf.findMedian(),mf.addNum(129),mf.findMedian(),mf.addNum(157),mf.findMedian(),mf.addNum(136),mf.findMedian(),mf.addNum(41),\
mf.findMedian(),mf.addNum(40),mf.findMedian(),mf.addNum(78),mf.findMedian(),mf.addNum(141),mf.findMedian(),mf.addNum(16),mf.findMedian(),mf.addNum(137),mf.findMedian(),mf.addNum(127),mf.findMedian(),mf.addNum(19),mf.findMedian(),\
mf.addNum(70),mf.findMedian(),mf.addNum(15),mf.findMedian(),mf.addNum(16),mf.findMedian(),mf.addNum(65),mf.findMedian(),mf.addNum(96),mf.findMedian(),mf.addNum(157),mf.findMedian(),mf.addNum(111),mf.findMedian(),mf.addNum(87),mf.findMedian(),mf.addNum(95),mf.findMedian(),mf.addNum(52),mf.findMedian(),mf.addNum(42),mf.findMedian(),mf.addNum(12),mf.findMedian(),mf.addNum(60),mf.findMedian(),mf.addNum(17),mf.findMedian(),mf.addNum(20),mf.findMedian(),mf.addNum(63),mf.findMedian(),mf.addNum(56),mf.findMedian(),mf.addNum(37),mf.findMedian(),mf.addNum(129),mf.findMedian(),mf.addNum(67),mf.findMedian(),mf.addNum(129),mf.findMedian(),mf.addNum(106),mf.findMedian(),mf.addNum(107),mf.findMedian(),mf.addNum(133),mf.findMedian(),mf.addNum(80),mf.findMedian(),mf.addNum(8),mf.findMedian(),mf.addNum(56),mf.findMedian(),mf.addNum(72),mf.findMedian(),mf.addNum(81),mf.findMedian(),mf.addNum(143),mf.findMedian(),mf.addNum(90),mf.findMedian(),mf.addNum(0),mf.findMedian()
'''

