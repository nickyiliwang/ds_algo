# Monotonic increasing
def largestRectangleArea(heights):
    res = 0
    stack = []

    for i, h in enumerate(heights):
        # what is this start index ?
        # we don't know we can extend backwards yet
        start = i

        while stack and h < stack[-1][1]:
            stackIndex, height = stack.pop()

            length = i - stackIndex
            res = max(res, height * length)

            # this height is greater than the current height we are visiting
            # extend the start index backwards to the index we just popped
            # I still don't get it
            start = stackIndex
        # adding the start index that we pushed all the way backwards
        stack.append((start, h))

    # might be entries in the stack, extended all the way to the end of the histogram, still need to compute the height

    for i, h in stack:
        res = max(res, h * (len(heights) - i))

    return res


heights = [2, 4]
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
