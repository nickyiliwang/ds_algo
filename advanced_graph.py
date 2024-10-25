from collections import *
from typing import List
import heapq


## reconstruct itinerary
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    adj = {src: [] for src, dst in tickets}
    res = []

    for src, dst in tickets:
        adj[src].append(dst)

    for key in adj:
        adj[key].sort()

    def dfs(adj, src):
        if src in adj:
            destinations = adj[src][:]
            while destinations:
                dest = destinations[0]
                adj[src].pop(0)
                dfs(adj, dest)
                destinations = adj[src][:]
        res.append(src)

    dfs(adj, "JFK")
    res.reverse()

    if len(res) != len(tickets) + 1:
        return []

    return res


## min cost to connect all points
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    N = len(points)
    adj = {i: [] for i in range(N)}
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, 4):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    res = 0
    visit = set()
    minH = [[0, 0]]
    while len(visit) < N:
        cost, i = heapq.heappop(minH)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])

    return res


## network delay time
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    edges = defaultdict(list)
    for u, v, w in times:
        edges[u].append((v, w))

    minHeap = [(0, k)]
    visit = set()
    t = 0
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        t = w1

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(minHeap, (w1 + w2, n2))

    return t if len(visit) == n else -1


## swim in rising water
def swimInWater(self, grid: List[List[int]]) -> int:
    N = len(grid)
    visit = set()
    minH = [[grid[0][0], 0, 0]]
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    visit.add((0, 0))
    while minH:
        t, r, c = heapq.heappop(minH)
        if r == N - 1 and c == N - 1:
            return t
        for dr, dc in directions:
            neiR, neiC = r + dr, c + dc
            if neiR < 0 or neiR == N or neiC == N or (neiR, neiC) in visit:
                continue
            visit.add((neiR, neiC))
            heapq.heappush(minH, [max(t, grid[neiR][neiC], neiR, neiC)])


## alien dictionary
def alienOrder(self, words: List[str]) -> str:
    adj = {char: set() for word in words for char in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visited = {}
    res = {}

    def dfs(char):
        if char in visited:
            return visited[char]

        visited[char] = True

        for neighChar in adj[char]:
            if dfs(neighChar):
                return True

        visited[char] = False
        res.append(char)

    for char in adj:
        if dfs(char):
            return ""

    res.reverse()
    return "".join(res)


## cheapest flights with k stops
def findCheapestPrice(
    self, n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    prices = [float("inf")] * n
    prices[src] = 0

    for i in range(k + 1):
        tmpPrices = prices.copy()

        for s, d, p in flights:
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmpPrices[d]:
                tmpPrices[d] = prices[s] + p
        prices = tmpPrices

    return -1 if prices[dst] == float("inf") else prices[dst]
