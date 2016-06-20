__author__ = 'Adward'
import bisect

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.numbers = []
        self.toSort = False

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        # self.numbers.insert(bisect.bisect_right(self.numbers, number), number)
        if len(self.numbers) > 0 and self.numbers[-1] > number:
            self.toSort = True
        self.numbers.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if self.toSort:
            self.numbers.sort()
            self.toSort = False
        if len(self.numbers) < 2 \
                or value < self.numbers[0] + self.numbers[1] \
                or value > self.numbers[-1] + self.numbers[-2]:
            return False
        index1 = 0
        index2 = bisect.bisect_right(self.numbers, value - self.numbers[0]) - 1
        odd_flag = True
        while True:
            if self.numbers[index1] + self.numbers[index2] != value:
                if index2 - index1 <= 1:
                    return False
                if odd_flag:
                    index1 = bisect.bisect_left(self.numbers,
                                                value - self.numbers[index2], index1+1, index2)
                else:
                    index2 = bisect.bisect_right(self.numbers,
                                                value - self.numbers[index1], index1+1, index2) - 1
                odd_flag = not odd_flag
            else:
                return True

        # return [index1+1, index2+1]



# Your TwoSum object will be instantiated and called as such:
twoSum = TwoSum()
twoSum.add(3)
twoSum.add(1)
twoSum.add(4)
print(twoSum.find(6))
# twoSum.find(value)