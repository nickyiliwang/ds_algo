# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

def twoSum(nums, target):
    # we can do this in one pass
    prevMap = {}  # val: index
    # enumerate gives the index and value of an iterative data structure
    for i, n in enumerate(nums):
        diff = target - n
        # x in dict
        # meaning we got a difference, return the index of the diff and the current index of the loop
        if diff in prevMap:
            return [prevMap[diff], i]

        # number val: index
        prevMap[n] = i
    return


twoSum([3, 3, 2, 1], 6)

# def twoSum(nums, target):
# # My solution with hashMap and cal for diff
# # O(n + n), relative complexity of O(n)
#     res = []
#     hashMap = {}
#     # get the hashMap
#     for x in range(len(nums)):
#         # key: number, value: index in arr
#         hashMap[nums[x]] = x

#     for x in range(len(nums)):
#         # 6 - 3 = 3
#         diff = target - nums[x]
#         # key in the hasMap check if the diff exist O(1), returns 1 or None
#         key = hashMap.get(diff)
#         # the key exist and the key index isn't the index of x (itself), we have a diff
#         if (key and hashMap[diff] != x):
#             res = [hashMap[diff],  x]

#     print(res)
#     return res


# brute force
# With nested loops, O(n^2)
# Output Limit Exceeded
# def twoSum(nums, target):
#     res = []
#     for x in range(len(nums)):
#         y = x + 1
#         while y <= len(nums) - 1:
#             print(nums[x] + nums[y])
#             if (nums[x] + nums[y] == target):
#                 res = [x, y]
#             y += 1

#     print(res)
#     return res
