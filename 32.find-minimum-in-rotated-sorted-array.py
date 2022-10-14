# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

from typing import List

# my solution


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    # no pivot
    if nums[left] < nums[right]:
        return nums[left]
    # if there is pivot
    # the left number will reach a point where
    # it's not bigger than the right more number
    # we don't touch right pointer
    while nums[left] > nums[right]:
        left = left + 1
    return nums[left]


nums = [3, 4, 5, 1, 2]
# Output: 11
findMin(nums)

# Neetcode, also great

# def findMin(nums: List[int]) -> int:
#     # default result
#     res = nums[0]
#     left, right = 0, len(nums) - 1

#     while left <= right:
#         # left most number is smaller than right most number
#         # sorted list no pivot
#         if nums[left] < nums[right]:
#             res = min(res, nums[left])
#             break

#         # we are not touching the right pointer
#         middle = (left + right) // 2
#         res = min(res, nums[middle])
#         # important part
#         # mid point will always bigger or equal to left
#         # this algo is efficient because we are cutting in half in every operation
#         if nums[left] <= nums[middle]:
#             left = middle + 1
#         else:
#             right = middle - 1
#     return res
