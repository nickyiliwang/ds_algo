# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:

# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

# Output:
# true
# Example 2:

# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

# Output:
# false
# Note:

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
# Constraints:

# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2


class Solution:
    def validTree(self, n: int, edges) -> bool:
        # KEY here is to check this
        if len(edges) < n-1:
            return False

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
                return False

            if rank[pX] > rank[pY]:
                parent[pX] = parent[pY]
            else:
                parent[pX] = parent[pY]
                rank[pY] += rank[pX]

            return True

        for x, y in edges:
            if union(x, y) == False:
                return False

        return True
