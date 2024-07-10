#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
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
from collections import Counter, deque


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [[-val, key] for key, val in Counter(tasks).items()]
        heapq.heapify(maxHeap)
        res = []

        while maxHeap:
            temp = []
            for _ in range(n + 1):
                if maxHeap:
                    task = heapq.heappop(maxHeap)
                    task[0] += 1
                    if task[0]:
                        temp.append(task)
                    res.append(task[1])
                else:
                    res.append("idle")

            for task in temp:
                heapq.heappush(maxHeap, task)

        while res[-1] == "idle":
            res.pop()

        return len(res)


# @lc code=end
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))


# Can't figure out when to increment the time
# because when I reach the end of the maxHeap
# there will still be n extra idle times at the end
def leastInterval(self, tasks: List[str], n: int) -> int:
    maxHeap = [[-val, key] for key, val in Counter(tasks).items()]
    heapq.heapify(maxHeap)
    times = 0

    while maxHeap:
        temp = []
        for _ in range(n + 1):
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task[0] += 1
                if task[0]:
                    temp.append(task)

            times += 1

        for task in temp:
            heapq.heappush(maxHeap, task)

    return times - n


# neetcode
def leastInterval(self, tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()  # pairs of [-cnt, idleTime]
    while maxHeap or q:
        time += 1

        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        else:
            time = q[0][1]

        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time
