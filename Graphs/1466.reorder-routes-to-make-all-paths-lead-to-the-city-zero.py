#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
#
# algorithms
# Medium (64.46%)
# Likes:    4109
# Dislikes: 117
# Total Accepted:    192.1K
# Total Submissions: 297.9K
# Testcase Example:  '6\n[[0,1],[1,3],[2,3],[4,0],[4,5]]'
#
# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there
# is only one way to travel between two different cities (this network form a
# tree). Last year, The ministry of transport decided to orient the roads in
# one direction because they are too narrow.
#
# Roads are represented by connections where connections[i] = [ai, bi]
# represents a road from city ai to city bi.
#
# This year, there will be a big event in the capital (city 0), and many people
# want to travel to this city.
#
# Your task consists of reorienting some roads such that each city can visit
# the city 0. Return the minimum number of edges changed.
#
# It's guaranteed that each city can reach city 0 after reorder.
#
#
# Example 1:
#
#
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node
# can reach the node 0 (capital).
#
#
# Example 2:
#
#
# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node
# can reach the node 0 (capital).
#
#
# Example 3:
#
#
# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0
#
#
#
# Constraints:
#
#
# 2 <= n <= 5 * 10^4
# connections.length == n - 1
# connections[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
#
#
#
# Keys:
# start at city zero
# recursively check its neighbors
# count outgoing edges
#

from typing import List

# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections} # set
        neighbors = {city: [] for city in range(n)}
        visited = set()
        res = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visited, res

            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    res += 1
                visited.add(neighbor)
                dfs(neighbor)

        visited.add(0)
        dfs(0)
        return res


# @lc code=end

print(Solution().minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
