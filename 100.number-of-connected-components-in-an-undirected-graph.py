# Count Connected Components
# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# Return the total number of connected components in that graph.

# Example 1:

# Input:
# n=3
# edges=[[0,1], [0,2]]

# Output:
# 1
# Example 2:

# Input:
# n=6
# edges=[[0,1], [1,2], [2, 3], [4, 5]]

# Output:
# 2
# Constraints:

# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2


from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n + 1)]
        rank = [i for i in range(n + 1)]

        def find(i):
            if parent[i] == i:
                return i
            else:
                return find(parent[i])

        def union(x, y):
            pX, pY = find(x), find(y)

            if pX == pY:
                return 0

            if rank[pX] > rank[pY]:
                parent[pX] = parent[pY]
            else:
                parent[pX] = parent[pY]
                rank[pY] += rank[pX]

            return 1

        res = n
        for x, y in edges:
            res -= union(x, y)

        return res
