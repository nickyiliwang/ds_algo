from collections import deque
from typing import List

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    left = right = 0
    # deque can popleft the beginning and add/remove at the end in constant time
    q = deque()

    # stop right before length of array, len is always index + 1
    while right < len(nums):
        # monotonic decreasing queue
        # pops all numbers at the end of the queue smaller than right pointer number
        while q and nums[q[-1]] < nums[right]:
            q.pop()

        # appending right index
        q.append(right)

        # if left pointer is bigger than the beginning index of deque
        # meaning we want to popleft the left val from the window
        if left > q[0]:
            q.popleft()

        # if we arrive at the sliding window
        # append the left most val to result
        # increment left pointer
        if (right - left + 1) == k:
            res.append(nums[q[0]])
            left += 1

        right += 1

    print(res)
    return res


maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)