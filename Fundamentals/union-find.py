class DisjointSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return

        if self.rank[parentX] < self.rank[parentY]:
            self.parent[parentX] = parentY
        elif self.rank[parentX] > self.rank[parentY]:
            self.parent[parentY] = parentX
        else:
            self.parent[parentY] = parentX
            self.rank[parentX] = self.rank[parentX] + 1


# Driver code
obj = DisjointSet(5)
obj.union(0, 2)
obj.union(4, 2)
obj.union(3, 1)

if obj.find(4) == obj.find(0):
    print("Yes")
else:
    print("No")
if obj.find(1) == obj.find(0):
    print("Yes")
else:
    print("No")
