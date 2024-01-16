#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.26%)
# Likes:    20584
# Dislikes: 618
# Total Accepted:    1.1M
# Total Submissions: 2.6M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
#
#
#


# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        res = 0
        prefixMap = {0: 1}

        for num in nums:
            sum += num
            diff = sum - k
            if diff in prefixMap:
                res += prefixMap[diff]

            prefixMap[sum] = prefixMap.get(sum, 0) + 1
        return res


# @lc code=end

# Keys:
# 0. Need the current sum every time for the diff
# 1. need to update the result on every compute
# 2. prefixMap stores the different prefixes that we can remove and result in an sum of k
# 3. update the prefixMap regardless

print(Solution.subarraySum("", [1, 1, 1], 2))
