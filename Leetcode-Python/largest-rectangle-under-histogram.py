__author__ = 'Adward'
class Solution(object):
    # Calculating maximum area when hist[x] as the current lowest bar:
    # - 1st bar lower than x on its left: index of previous bar in the stack
    # - 1st bar lower than x on its right: index of current bar that triggers stack popping
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Create an empty stack. The stack holds indexes of hist[] array
        # The bars stored in stack are always in increasing order of their heights
        stk = []
        maxArea = i = 0
        while i < len(heights):
            # If this bar is higher than the bar on top of the stack, push it to stack
            if len(stk) == 0 or heights[stk[-1]] <= heights[i]:
                stk.append(i)
                i += 1
            else:  # If lower than last bar on stack, pop & don't move on to the next bar
                # Calculate the area with hist[stk[-1]] stack as lowest bar
                curArea = heights[stk.pop()] * (i - stk[-1] - 1 if len(stk) else i)
                maxArea = max(curArea, maxArea)

        # Now pop the remaining bars from stack and calculate area with every
        # popped bar as the smallest bar
        while len(stk):
            curArea = heights[stk.pop()] * (i - stk[-1] - 1 if len(stk) else i)
            maxArea = max(curArea, maxArea)

        return maxArea

sol = Solution()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))