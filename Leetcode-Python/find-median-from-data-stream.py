__author__ = 'Adward'
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 0
        self.layerN = 1
        self.maxP = 0
        self.tree = [None]

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """

        self.N += 1
        if not self.tree[0]:
            self.tree[0] = [num, 1, 0, 0]
        else:
            p = 0
            while p <= self.maxP and self.tree[p]:
                pnum = self.tree[p][0]
                if num == pnum:
                    self.tree[p][1] += 1
                    return
                elif num < pnum:
                    self.tree[p][2] += 1
                    p = p * 2 + 1
                else:
                    self.tree[p][3] += 1
                    p = p * 2 + 2
            if p > self.maxP:
                self.tree += [None] * (2**self.layerN)
                self.layerN += 1
                self.maxP = 2 ** self.layerN - 2
            self.tree[p] = [num, 1, 0, 0]


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.N == 0:
            return 0
        mid = (self.N - 1) // 2
        p = 0
        base = 0
        while p <= self.maxP:
            num, mmid, lleft, rright = self.tree[p]
            if base + lleft - 1 >= mid:
                p = p * 2 + 1
            elif base + lleft + mmid - 1 >= mid:
                if self.N % 2 or base + lleft + mmid - 1 > mid:
                    return num
                else:
                    p = p * 2 + 2
                    lp = p * 2 + 1
                    while lp <= self.maxP and self.tree[lp]:
                        p = lp
                        lp = p * 2 + 1
                    try:
                        nnum = self.tree[p][0]
                    except:
                        p = (p-2) // 2
                        nnum = self.tree[p//2][0]
                    return (num + nnum) / 2
            else:
                p = p * 2 + 2
                base += lleft + mmid
        return 0


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(155),mf.findMedian(),mf.addNum(66),mf.findMedian(),mf.addNum(114),mf.findMedian(),mf.addNum(0),mf.findMedian(),mf.addNum(60),mf.findMedian(),mf.addNum(73),mf.findMedian(),mf.addNum(109),mf.findMedian(),mf.addNum(26),mf.findMedian(),mf.addNum(154),mf.findMedian(),mf.addNum(0),mf.findMedian(),mf.addNum(107),mf.findMedian(),mf.addNum(75),mf.findMedian(),mf.addNum(9)
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