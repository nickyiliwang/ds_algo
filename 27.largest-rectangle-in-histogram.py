def largestRectangleArea(heights):
    heights.append(0)
    stack = [-1]
    res = 0

    for i, curr in enumerate(heights):
        while heights[stack[-1]] > curr:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            res = max(res, h * w)

        stack.append(i)

    return res


# Monotonic Decreasing Stack
def largestRectangleArea(heights):
    # The heights of 0 is appended to the end of the heights list to handle the case where the stack is not empty after the iterations.
    heights.append(0)
    stack = [-1]
    res = 0

    for i, curr in enumerate(heights):
        # At each iteration, it checks if the current heights is less than the heights at the top of the stack.
        while heights[stack[-1]] > curr:
            # If it is, it pops the heights at the top of the stack and calculates the area of the rectangle represented by that heights and the width of the rectangle (which is the difference between the current index and the index at the top of the stack).
            h = heights[stack.pop()]

            w = i - stack[-1] - 1
            res = max(res, h * w)

        stack.append(i)

    return res

# how come there's always one element left in the stack at the end of the function loop ?
# The reason there is always one element left in the stack at the end of the function loop is because the code always appends the current index (i) to the stack, regardless of whether it is smaller or larger than the previous height. The stack will always have at least one element in it, which corresponds to the index of the last height in the list.

# Additionally, the while loop continues to pop elements off the stack as long as the current height is smaller than the previous height on top of the stack. Even if the current height is larger than the previous height, it will still be appended to the stack, leaving one element left in the stack at the end of the function loop.

# heights[stack[-1]]
# in the first iteration, heights[stack[-1]] => heights[-1] => 0 because we appended the 0 to the end of the list

# w = i - stack[-1] - 1
# if there's no elements in the heights list, the loop runs and end, but if there is one+ element, like [1]. The index will run up to 1, and w = i - stack[-1] - 1 => w = 1 - (-1) - 1 => w = 2 - 1 => 1 for the width.

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
