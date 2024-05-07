#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
#
#
# Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
#
#
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]

                w = i - stack[-1] - 1

                res = max(res, h * w)

            stack.append(i)

        return res


# @lc code=end

# Monotonic Increasing Stack
def largestRectangleArea(heights):
    # The 0 will clear the stack (because 0 > -1) after the heights are iterated
    heights.append(0)
    stack = [-1]
    res = 0

    for i, curr in enumerate(heights):
        while heights[stack[-1]] > curr:
            h = heights[stack.pop()]

            # By subtracting 1 from the difference we exclude the current position from the width calculation, as the width is determined by the elements to the left of the current element.
            w = i - stack[-1] - 1
            res = max(res, h * w)

        stack.append(i)

    return res

# how come there's always one element left in the stack at the end of the function loop ?
# Because the code always appends the current index (i) to the stack, regardless of whether it is smaller or larger than the previous height. The stack will always have at least one element in it, which corresponds to the index of the last height in the list.

# Additionally, the while loop continues to pop elements off the stack as long as the current height is smaller than the previous height on top of the stack. If the current height is larger than the previous height, it appends to the stack

# heights[stack[-1]]
# in the first iteration, heights[stack[-1]] => heights[-1] => 0 because we appended the 0 to the end of the list

# w = i - stack[-1] - 1
# if there's no elements in the heights list, the loop runs and end, but if there is one+ element, like [1]. The index will run up to 1, and w = i - stack[-1] - 1 => w = 1 - (-1) - 1 => w = 2 - 1 => 1 for the width.
