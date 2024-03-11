# 547. Number of Provinces
# Medium
# Topics
# Companies
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3


# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

from typing import List


# non working solution
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(i):
            if parent[i] == i:
                return i
            else:
                return find(parent[i])

        def union(x, y):
            pX, pY = find(x), find(y)

            if pX == pY:
                return 0

            if parent[pX] < parent[pY]:
                parent[pY] = parent[pX]
            elif parent[pX] > parent[pY]:
                parent[pX] = parent[pY]
            else:
                parent[pX] = parent[pY]
                rank[pY] += rank[pX] + 1

            return 1

        res = n + 1
        for r in range(n):
            for c in range(n):
                res -= union(r, c)

        return res


print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
