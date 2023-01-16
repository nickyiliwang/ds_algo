def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    leftMax, rightMax = height[left], height[right]
    res = 0

    while left < right:
        if (leftMax <= rightMax):
            left += 1
            leftMax = max(leftMax, height[left])

            res += leftMax - height[left]

        else:
            right -= 1
            if (rightMax - height[right]) > 0:
                res += rightMax - height[right]

            rightMax = max(rightMax, height[right])

    return res


# for each position, we want the leftMax value and rightMax value and get the maximum rain water we can trap in the current position
# we can also do one pass to get all the leftMax and rightMax for each rain water position

# Explanation:
# min value of (leftMax, rightMax) - height value will get you the amount of rain drop this container can hold
# result:    [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0] => 6
# input:     [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# leftMax:   [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
# rightMax:  [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
# min(L, R): [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]


# Pointer solution
# But the idea is correct with min value of (leftMax, rightMax) - height value will get you the amount of rain drop this container can hold
def trap(height):
    # if the value is not empty or not False.
    if not height:
        return 0

    left, right = 0, len(height) - 1
    # leftMax height, and rightMax height
    leftMax, rightMax = height[left], height[right]
    res = 0

    while left < right:
        # this if else ensures that we are always moving the lower pointer
        if (leftMax <= rightMax):
            # update left pointer
            left += 1
            # we don't need the rightMax value because rightMax value isn't reliable
            # leftMax value is also the bottleneck anyways, ie. min(leftMax, rightMax)
            # to update the leftMax value, we take the current leftMax, and height[left] (future leftMax)

            # leftMax will always want to be the highest number before the left pointer
            # if we update the leftMax number before the calculation we can avoid negative numbers
            # if the current left pointer has the highest left max then we want to update leftMax to current max height
            # Because there is no point in getting the previous leftMax when the current hight is taller, meaning we will get a negative number
            leftMax = max(leftMax, height[left])

            res += leftMax - height[left]

        else:
            right -= 1

            if (rightMax - height[right]) > 0:
                res += rightMax - height[right]

            rightMax = max(rightMax, height[right])

    return res

# # Time Limit Exceeded Pointer Solution
# # But the idea is correct with min value of (leftMax, rightMax) - height value will get you the amount of rain drop this container can hold
# def trap(height):
#     res = 0

#     for i, n in enumerate(height):
#         leftMax = 0
#         rightMax = 0

#         # [1, 2, 3][:2] => [1, 2]
#         # a[:stop] stops before the index so we don't need -1

#         if len(height[:i]) > 0:
#             leftMax = max(height[:i])

#         # [1, 2, 3][2:] => [3]
#         # a[:start] starts from the index so we do need i + 1
#         # The reason we do i+1 here is because we don't want the number itself to be included
#         if len(height[i+1:]) > 0:
#             rightMax = max(height[i+1:])

#         minOfLeftAndRight = min(leftMax, rightMax)
#         if (minOfLeftAndRight - height[i]) > 0:
#             res = res + (minOfLeftAndRight - height[i])

#     return res

# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# trap(height)
