#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#
# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
#
# algorithms
# Easy (71.97%)
# Likes:    3057
# Dislikes: 126
# Total Accepted:    173.7K
# Total Submissions: 229.7K
# Testcase Example:  '[1,1,2,2,2,3]'
#
# Given an array of integers nums, sort the array in increasing order based on
# the frequency of the values. If multiple values have the same frequency, sort
# them in decreasing order.
#
# Return the sorted array.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has
# a frequency of 3.
#
#
# Example 2:
#
#
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in
# decreasing order.
#
#
# Example 3:
#
#
# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
#
#
#


from collections import Counter
import heapq
from typing import List


# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        bucket = [[] for _ in range(len(nums))]
        c = Counter(nums)
        for key, freq in c.items():
            for _ in range(freq):
                if bucket[freq-1] and bucket[freq-1][-1] > key:
                    bucket[freq-1].append(key)
                else:
                    bucket[freq-1].insert(0,key)
        res = []
        for l in bucket:
            if l:
                res += l
        return res




# @lc code=end

print(Solution().frequencySort([1,5,0,5]))
# [1,0,5,5]