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


# Stack solution
# monotonic increasing
def largestRectangleArea(heights):


heights = [2, 1, 5, 6, 2, 3]
# Output: 10
largestRectangleArea(heights)


# # Brute force
# def largestRectangleArea(heights):
#     res = []
#     for i, n in enumerate(heights):
#         # get all the possible areas for each number in the heights
#         temp = []
#         # append itself first
#         temp.append(n)
#         # ignoring itself
#         whileIndex = i + 1
#         # Loop over the rest of the numbers
#         while whileIndex < len(heights):
#             # the min height
#             # i:whileIndex + 1 fixes the off by one error
#             minHeight = min(heights[i:whileIndex + 1])
#             length = whileIndex - i + 1

#             area = minHeight * length
#             temp.append(area)
#             whileIndex += 1
#         res.append(temp)

#     finalRes = []
#     for n in res:
#         finalRes.append(max(n))

#     print(max(finalRes))
#     return max(finalRes)


# heights = [2, 1, 5, 6, 2, 3]
# # Output: 10
# largestRectangleArea(heights)

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
