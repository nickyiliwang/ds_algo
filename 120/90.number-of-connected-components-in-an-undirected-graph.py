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

# Key:
# 0 for false
# 1 for true
# res start with max components and as they connect decrease accordingly

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [i for i in range(n)]

        def find(i):
            if parent[i] == i:
                return i
            else:
                return find(parent[i])

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return 0

            if rank[px] > rank[py]:
                parent[px] = parent[py]
            else:
                parent[px] = py
                rank[py] += 1

            return 1

        res = n

        for x, y in edges:
            res -= union(x, y)

        return res
