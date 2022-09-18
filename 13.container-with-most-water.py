# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# linear time:
# my solution after watching explanation
# mine is more readable
# we are always going to move the shorter end of the point, because it's the bottleneck
def maxArea(height):
    res = 0
    left, right = 0, len(height) - 1

    while left < right:
        length = right - left
        maxHeight = min(height[left], height[right])
        area = length * maxHeight
        res = max(res, area)

        if height[left] <= height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1

    print(res)
    return res


maxArea([1, 8, 100, 2, 100, 4, 8, 3, 7])

# # my solution after watching explanation
# def maxArea(height):
#     l, r = 0, len(height) - 1
#     res = 0

#     while l < r:
#         res = max(res, min(height[l], height[r]) * (r - l))
#         if height[l] < height[r]:
#             l += 1
#         elif height[r] <= height[l]:
#             r -= 1
#     print(res)
#     return res


# maxArea([1, 8, 100, 2, 100, 4, 8, 3, 7])


# # Brute force O(n ^ 2)
# def maxArea(height):
#     res = 0
#     for l in range(len(height)):
#         for r in range(l + 1, len(height)):
#             area = (r - l) * min(height[l], height[r])
#             res = max(res, area)

#     print(res)
#     return res


# maxArea([2, 3, 4, 5, 18, 17, 6])

# # my solution
# # we want to compare areas
# # how do I get all the areas
# # this one cannot be sorted
# # from doing this solution, I realize that my loops does not cover all the possibilities

# def maxArea(height):
#     left, right = 0, len(height) - 1
#     res = 0

#     # moving left pointer to the right, calc all area
#     while left < right:
#         length = right - left
#         maxHeight = min(height[left], height[right])

#         maxArea = length * maxHeight
#         print("left", maxArea)
#         if res < maxArea:
#             res = maxArea

#         left += 1

#     # move right pointer to the left, cal all area
#     left, right = 0, len(height) - 1
#     while left < right:
#         length = right - left
#         maxHeight = min(height[left], height[right])

#         maxArea = length * maxHeight
#         print("right", maxArea)

#         if res < maxArea:
#             res = maxArea

#         right -= 1

#     # move left and right pointer together
#     left, right = 0, len(height) - 1
#     while left < right:
#         length = right - left
#         maxHeight = min(height[left], height[right])

#         maxArea = length * maxHeight
#         print("center", maxArea)

#         if res < maxArea:
#             res = maxArea

#         left += 1
#         right -= 1

#     # check individuals
#     left, right = 0, len(height) - 1
#     while left < right:
#         length = left + 1 - left
#         maxHeight = min(height[left], height[left + 1])

#         maxArea = length * maxHeight

#         if res < maxArea:
#             res = maxArea

#         left += 1

#     print(res)
#     return res


# maxArea([2, 3, 4, 5, 18, 17, 6])
