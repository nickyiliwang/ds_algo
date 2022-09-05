from typing import List


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# neetcode
def productExceptSelf(nums: List[int]) -> List[int]:
    # So we are at idx 3, prefix), post fix 4
    # prefix: every number before 3 = [1,2]
    # postfix: every number after 3 = [4]

    # in the context of this problem
    # this result array does not count for memory complexity
    res = [1] * len(nums)
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)

    for x in range(len(prefix)):
        # we want to stop before going out of bounds
        if (x + 1 < len(prefix)):
            # prefix * nums number at x inx will be the number in x + 1
            # nums array will stop at last idx in this pass
            prefix[x + 1] = prefix[x] * nums[x]

    # python reverse range with range(len(x) - 1, -1, -1), the stop will stop before -1 meaning it reached 0 idx
    for x in range(len(prefix) - 1, -1, -1):

    print(prefix)


nums = [4, 5, 1, 8, 2]
productExceptSelf(nums)

# # brute force
# def productExceptSelf(nums: List[int]) -> List[int]:
#     res = []

#     for x in range(len(nums)):
#         sum = 1
#         print(x)

#         for y in range(len(nums)):
#             if (x != y):
#                 sum = sum * nums[y]
#                 # print(sum)
#         res.append(sum)
#     print(res)
#     return res
# nums = [1, -1]
# productExceptSelf(nums)
