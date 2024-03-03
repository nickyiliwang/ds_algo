#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (46.56%)
# Likes:    15792
# Dislikes: 669
# Total Accepted:    1.5M
# Total Submissions: 3.2M
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
from typing import List


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        validator = [[] for _ in range(numCourses)]
        visited = set()

        for course, pre in prerequisites:
            validator[course].append(pre)

        def dfs(course):
            if course in visited:
                return False

            if validator[course] == []:
                return True

            visited.add(course)
            for pre in validator[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            validator[course] = []
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return False

        return True


# @lc code=end

print(Solution().canFinish(2, [[1, 0]]))
