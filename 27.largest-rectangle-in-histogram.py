# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

#  A histogram is a graph that shows the frequency of numerical data using rectangles. The height of a rectangle (the vertical axis) represents the distribution frequency of a variable (the amount, or how often that variable appears).


# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4


# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

# 
def largestRectangleArea(heights):
    res = []
    for i, n in enumerate(heights):
        temp = []
        temp.append(n)
        whileIndex = i + 1
        while whileIndex < len(heights):
            minHeight = min(heights[i:whileIndex])
            length = whileIndex - i + 1
            
            area = minHeight * length
            temp.append(area)
            whileIndex += 1
        res.append(temp)
    print(res)
    return res


heights = [2, 1, 5, 6, 2, 3]
largestRectangleArea(heights)

# # two pointer attempt
# # This did not work because we can't use the areas, the small numbers in between two pointer is the real gating number to calculate area, instead of water container
# def largestRectangleArea(heights):
#     res = 0
#     left, right = 0, len(heights) - 1

#     while left < right:
#         length = right - left

#         maxHeight = min(heights[left], heights[right])
#         maxArea = length * maxHeight
#         res = max(res, maxArea)

#         # keep finding the higher side
#         if heights[left] <= heights[right]:
#             left += 1
#         elif heights[left] > heights[right]:
#             right -= 1

#     res = max(res, max(heights))
#     print(res)
#     return res


# heights = [2, 1, 5, 6, 2, 3]
# largestRectangleArea(heights)
