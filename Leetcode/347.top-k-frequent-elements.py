#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (62.75%)
# Likes:    16985
# Dislikes: 635
# Total Accepted:    2.1M
# Total Submissions: 3.3M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#
from typing import List
from collections import Counter


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums))]
        counters = Counter(nums)
        res = []

        for num, count in counters.items():
            bucket[count - 1].append(num)

        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


# @lc code=end
