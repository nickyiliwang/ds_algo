from collections import deque


def maxSlidingWindow(nums, k):
    q = collections.deque()
    res = []
    left = 0

    for right, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(right)

        if left > q[0]:
            q.popleft()

        if right - left + 1 == k:
            res.append(nums[q[0]])
            left += 1
    return res

# Explanation
def maxSlidingWindow(nums, k):
    q = collections.deque()
    res = []
    left = 0

    for right, cur in enumerate(nums):
        # monotonic decreasing queue
        # pops all numbers at the end of the queue smaller than right pointer number
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(right)

        # remove first element if it's outside the window
        if left > q[0]:
            q.popleft()

        # if we arrive at the sliding window k
        # 1st elem will always be largest
        # increment left pointer, for loop will increment right pointer
        if right - left + 1 == k:
            res.append(nums[q[0]])
            left += 1
    return res


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
