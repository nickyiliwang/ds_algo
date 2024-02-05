import heapq

# min heap: smallest node at the top of the tree
#   4
# 10  5

# max heap:
#    10
#  5    4

data = [1, 3, 29087809, 325, 2, 5, 4, 46, 3, 5, 35, 345, 3, 6, 2, 54, 2346, 3, 63, 6]
heapq.heapify(data)
popped = heapq.heappop(data)
print(popped)
print(data)
# heapify op is logarithmic
# normal inserting to array is O(n) complexity
