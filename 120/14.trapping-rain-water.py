#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#
from typing import List

# Key:
# We want the leftMax value and rightMax value and get the maximum rain water we can trap in the left or right position
# Comparing leftMax and rightMax and move the smaller value 

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max, res = 0, 0, 0
        l, r = 0, len(height) - 1

        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if l_max < r_max:
                res += l_max - height[l]
                l += 1
            else:
                res += r_max - height[r]
                r -= 1

        return res


# @lc code=end

