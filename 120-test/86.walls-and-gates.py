# You are given a
# m×n 2D grid initialized with these three possible values:

# -1 - Wall or an obstacle
# 0 - A Gate
# INF - Empty room, 2147483647 represents it.

# Fill each land cell with the dist to its nearest gate. If a land cell cannot reach a treasure chest than the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is one of {-1, 0, 2147483647}

from typing import List
from collections import deque

# Multi value BFS

# start with the treasure/doors first
# update the dist in the while => forloop

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        rowBound, colBound = range(row), range(col)
        q = deque()
        visited = set()
        dist = 0

        # Like rotting orange, capture all doors/treasures first
        for r in rowBound:
            for c in colBound:
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        def mod(r, c):
            if (
                r not in rowBound
                or c not in colBound
                or (r, c) in visited
                or grid[r][c] == -1
            ):
                return

            visited.add((r, c))
            q.append([r, c])

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                mod(r + 1, c)
                mod(r - 1, c)
                mod(r, c + 1)
                mod(r, c - 1)

            dist += 1


print(
    Solution().islandsAndTreasure(
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    )
)
