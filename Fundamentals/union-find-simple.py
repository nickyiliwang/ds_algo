class DisjointedSet():
    def unionFind(self, n: int, edges) -> int:
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

            if rank[pX] < rank[pY]:
                parent[pY] = parent[pX]
            elif rank[pX] > rank[pY]:
                parent[pX] = parent[pY]
            else:
                parent[pX] = parent[pY]
                rank[pY] = rank[pX] + 1

            return 1

        res = n
        for x, y in edges:
            res -= union(x, y)

        return res
