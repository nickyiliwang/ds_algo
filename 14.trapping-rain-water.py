# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# for each position, we want the maxLeft value and maxRight value and get the maximum rain water we can trap in the current position
# we can also do one pass to get all the maxLeft and maxRight for each rain water position

def trap(height):
    maxLeft = []
    maxRight = []

    for i, n in enumerate(height):
        if len(height[:i]) > 0:
            maxLeft.append(max(height[:i]))
        else:
            maxLeft.append(0)

        if len(height[i:]) > 0:
            maxRight.append(max(height[i:]))
        else:
            maxRight.append(0)
        print(height[i:])

    # print(maxLeft, maxRight)
    print(maxRight)


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trap(height)
