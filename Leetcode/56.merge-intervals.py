#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#

# Keys:
# sort by the start of interval
# prevEnd needs to be smaller than the currStart (no overlap)
# else merge by taking the max of the 2 ends


# @lc code=start
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prevEnd = res[-1][1]
            if prevEnd < start:
                res.append([start, end])
            else:
                res[-1][1] = max(prevEnd, end)

        return res


# @lc code=end

print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
