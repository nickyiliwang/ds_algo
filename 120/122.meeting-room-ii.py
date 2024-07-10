# Meeting Schedule II
# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

# Example 1:

# Input: intervals = [(0,40),(5,10),(15,20)]

# Output: 2
# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)

# Example 2:

# Input: intervals = [(4,9)]

# Output: 1
# Note:

# (0,8),(8,10) is not considered a conflict at 8
# Constraints:

# 0 <= intervals.length <= 100
# 0 <= intervals[i].start < intervals[i].end <= 1000

# Key
# start is pos
# end is neg
# sort by both
# keep a count and maxCount, update by both 

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        currCount = 0
        maxCount = 0
        for start, end in intervals:
            times.append([start,1])
            times.append([end,-1])
        
        times.sort(key=lambda i:(i[0],i[1]))
        for t, c in times:
            currCount += c
            
            maxCount = max(maxCount, currCount)

        return maxCount
            
            


print(Solution().minMeetingRooms([(0, 40), (5, 10), (15, 20)]))
