#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (58.15%)
# Likes:    9311
# Dislikes: 1937
# Total Accepted:    502.7K
# Total Submissions: 864.5K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any
# order. Each task is done in one unit of time. For each unit of time, the CPU
# could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown
# period between two same tasks (the same letter in the array), that is that
# there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish
# all the given tasks.
#
#
# Example 1:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
#
#
# Example 2:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
#
#
# Example 3:
#
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#
#
#
# Constraints:
#
#
# 1 <= task.length <= 10^4
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].
#
#
#

from typing import List
import heapq


# MY passing solution
# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        maxHeap = []
        counter = {}
        res = []
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        for key, val in counter.items():
            maxHeap.append([-abs(val), key])

        heapq.heapify(maxHeap)

        while len(maxHeap) > 0:
            temp = []
            for _ in range(n + 1):
                if len(maxHeap) > 0:
                    secondaryTask = heapq.heappop(maxHeap)
                    secondaryTask[0] += 1
                    if secondaryTask[0] != 0:
                        temp.append(secondaryTask)
                    res.append(secondaryTask[1])
                else:
                    if len(maxHeap) == 0:
                        res.append("idle")
            for item in temp:
                heapq.heappush(maxHeap, item)

        while res[-1] == "idle":
            res.pop()

        return len(res)


# @lc code=end
print(
    Solution().leastInterval(
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
    )
)
