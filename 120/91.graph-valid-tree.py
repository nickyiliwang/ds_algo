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

# union find
from typing import *
from collections import *

class Solution:
    def validTree(self, n: int, edges) -> bool:
        visited = set()
        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for n in adj[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n


# union find
class Solution:
    def validTree(self, n: int, edges) -> bool:
        # edges will need to match num of nodes
        if len(edges) < n - 1:
            return False

        parent = [i for i in range(n)]
        rank = [i for i in range(n)]

        def find(i):
            if parent[i] == i:
                return i
            else:
                # recur finding parent
                return find(parent[i])

        def union(x, y):
            # find parent nodes
            px, py = find(x), find(y)

            if px == py:
                return False

            # the larger rank tree becomes the parent, and the ranks of x and y do not change
            if rank[px] > rank[py]:
                parent[px] = parent[py]
            else:
                # if y/x becomes root, increment their rank
                parent[px] = py
                rank[py] += 1

            return True

        for x, y in edges:
            if not union(x, y):
                return False

        return True
