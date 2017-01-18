__author__ = 'Adward'
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = []
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        self.cache.append(val)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        if len(self.cache) == 0:
            return self.intervals

        intervals2 = []
        for num in sorted(self.cache):
            if len(intervals2) == 0 or num > intervals2[-1].end + 1:
                intervals2.append(Interval(num, num))
            elif num == intervals2[-1].end + 1:
                intervals2[-1].end += 1
        self.cache = []

        i = j = 0
        ans = []
        intervals1 = self.intervals

        while True:
            if j < len(intervals2):
                if i == len(intervals1) or (i < len(intervals1) and intervals1[i].start > intervals2[j].start):
                    intervals1, intervals2 = intervals2, intervals1
                    i, j = j, i
            elif i == len(intervals1):
                break

            if len(ans) == 0 or intervals1[i].start > ans[-1].end + 1:
                ans.append(intervals1[i])
            else:
                ans[-1].end = max(ans[-1].end, intervals1[i].end)

            i += 1

        self.intervals = ans
        return ans


# Your SummaryRanges object will be instantiated and called as such:
def print_intervals(intvl):
    print([[i.start, i.end] for i in intvl])

obj = SummaryRanges()
obj.addNum(1)
print_intervals(obj.getIntervals())
obj.addNum(3)
print_intervals(obj.getIntervals())
obj.addNum(7)
print_intervals(obj.getIntervals())
obj.addNum(2)
print_intervals(obj.getIntervals())
obj.addNum(6)
print_intervals(obj.getIntervals())