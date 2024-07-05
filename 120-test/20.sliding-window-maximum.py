#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
#
# Return the max sliding window.
#
#
# Example 1:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        q = deque()

        for right, rightVal in enumerate(nums):
            while q and nums[q[-1]] <= rightVal:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if right - left + 1 == k:
                res.append(nums[q[0]])
                left += 1

        return res


# @lc code=end


# Key
def maxSlidingWindow(nums, k):
    q = deque()
    res = []
    left = 0

    for right, rightVal in enumerate(nums):
        # monotonic decreasing queue
        # pops all numbers at the end of the queue smaller than right pointer number
        while q and nums[q[-1]] <= rightVal:
            q.pop()

        q.append(right)

        # its out of bounds if the left pointer is bigger than first index item in q
        if left > q[0]:
            q.popleft()

        # if we arrive at the sliding window k
        # 1st elem will always be largest
        if right - left + 1 == k:
            res.append(nums[q[0]])
            left += 1
    return res


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
