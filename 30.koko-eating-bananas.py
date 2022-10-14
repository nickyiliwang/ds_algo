# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    # left could start at 0 or 1, doesn't really matter
    # one is more efficient
    left, right = 1, max(piles)
    # rate of eating starts at max
    # because it will always work but not in h hour
    res = max(piles)

    # important:
    # you will get off by one error if you don't set left is less or equal to right here

    while left <= right:
        # hours of eating
        hours = 0
        # mid point
        k = (left + right) // 2
        # eat the bananas and add on to the hours
        for b in piles:
            # math.ceil rounds up the result
            # math.ceil(5 / 5) = 1
            hours = hours + math.ceil(b / k)
        # if the the current rate of speed is less or equal to h(guard comes back)
        # we have a valid k
        # let's see if we can go lower by setting the right pointer to the mid point - 1
        if hours <= h:
            res = min(res, k)
            right = k - 1
        # too large
        # set the left pointer to mid point + 1
        else:
            left = k + 1
    print(res)
    return res


piles = [3, 6, 7, 11]
h = 8
# Output: 4
minEatingSpeed(piles, h)
