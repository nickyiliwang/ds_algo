#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

from typing import List

# Key:
# sort it
# continue for too big of number, and prev number is the same as curr
# l = n + 1, do 2pointer search
# once find, still need to find other instances for n with while loop, check prev and less than r


# Time nested loop + sorting =  nest loop worst time
# Time O(n ^ 2) + O(nlogn) =  O(n ^ 2)
# Space: O(1), O(n) depends on sorting implementation

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                currSum = n + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


# @lc code=end


def threeSum(nums):
    res = []

    # with a sorted array we can then use pointers
    nums.sort()

    if len(nums) < 3:
        return []

    for i, n in enumerate(nums):
        # if index is bigger than 0 and index value (ie. nums[0] == nums[1]) is a duplicate
        # go next iteration
        if i > 0 and n == nums[i - 1]:
            print("go next", i, n, nums[i - 1])
            continue

        # using pointers
        # moving left and right pointers like two sum
        # but we calculate the sum of 3 numbers
        # left pointer will always be current index + 1
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = n + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1

            else:
                # found pair, appending to res
                res.append([n, nums[l], nums[r]])
                # Remember to increment by one after the result is appended
                l += 1

                # while current left pointer is the same as the previous left pointer value
                # left index does not meet right index
                # increment it
                # ** Why do we not do the same for the right pointer ?
                # Because we only need to check left, if the right point is too large twice, our previous if statement will adjust it, ie. [1,2,3,5,5], it's just gonna move right pointer left twice if sum is bigger than 0
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                # [-2, -2, 0, 0, 2, 2]
    return res
