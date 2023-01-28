class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return val

    def _bubble_up(self, idx):
        if idx == 0:
            return
        parent_idx = (idx - 1) // 2
        if self.heap[parent_idx] > self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = (
                self.heap[idx],
                self.heap[parent_idx],
            )
            self._bubble_up(parent_idx)

    def _bubble_down(self, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        min_idx = idx
        if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[min_idx]:
            min_idx = left_idx
        if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[min_idx]:
            min_idx = right_idx
        if min_idx != idx:
            self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
            self._bubble_down(min_idx)


# Complete binary tree
# meaning if no left child, no right child for sure
# restoration after insertion with bubbling

# BigO(log k) k is the level of the heap
# bubbling up or down to restore the heap is the main operations

minHeap = MinHeap()

minHeap.push(10)
minHeap.push(4)
minHeap.push(15)
minHeap.pop()
minHeap.push(20)
minHeap.push(0)
minHeap.push(30)
minHeap.pop()
minHeap.pop()
minHeap.push(2)
minHeap.push(4)
minHeap.push(-1)
minHeap.push(-3)

print(minHeap.heap)
