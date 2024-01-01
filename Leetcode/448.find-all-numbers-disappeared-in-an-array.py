#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (60.59%)
# Likes:    9141
# Dislikes: 462
# Total Accepted:    821K
# Total Submissions: 1.4M
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in
# nums.
#
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
#
#
#
# Follow up: Could you do it without extra space and in O(n) runtime? You may
# assume the returned list does not count as extra space.
#
#


# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            n = abs(n) - 1
            nums[n] = -1 * abs(nums[n])

        res = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                res.append(i + 1)

        return res


# @lc code=end


print(Solution.findDisappearedNumbers("", [1, 1]))

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]


# My solution with using extra spaces
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        maxNum = max(nums)
        maxNum = max(maxNum, length)

        nums = set(nums)

        for n in range(maxNum):
            key = n + 1
            if key in nums:
                nums.remove(key)
            else:
                nums.add(key)

        return list(nums)
