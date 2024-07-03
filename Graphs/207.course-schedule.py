#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (47.02%)
# Likes:    16092
# Dislikes: 706
# Total Accepted:    1.6M
# Total Submissions: 3.4M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
#
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
#
#
# Return true if you can finish all courses. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
#
#
from collections import defaultdict


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        db = defaultdict(list)
        cycle, visited = set(), set()

        for crs, pre in prerequisites:
            db[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in db[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


# @lc code=end
