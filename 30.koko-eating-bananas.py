def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    res = max(piles)

    while left <= right:
        totalHours = 0
        mid = (left + right) // 2
        for b in piles:
            totalHours = totalHours + math.ceil(b / mid)
        if totalHours <= h:
            res = min(res, mid)
            right = mid - 1
        else:
            left = mid + 1
    return res


import math
from typing import List


# O(n log n)
def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    # rate of eating starts at max
    # because it will always work but not in h hour
    res = max(piles)

    while left <= right:
        # clears totalHours after each loop
        totalHours = 0
        mid = (left + right) // 2
        # eat the bananas and add on to the totalHours
        for b in piles:
            # math.ceil rounds up the result
            # 3.24 rounded to 4.0
            # rounding up here because anything over will take an extra turn
            # 7 / 6 = 1.666... = 2 turns
            totalHours = totalHours + math.ceil(b / mid)
        # ***usually we use mid point to the a value in nums to compare
        # ***here we use totalHours instead
        # totalHours <= h means a rate within h hours, means we are eating fast
        # right = mid - 1 to see if we can eat slower =>
        if totalHours <= h:
            res = min(res, mid)
            right = mid - 1
        else:
            # If the total number of hours is greater than h, it means that the current eating speed (mid) is not possible and the next iteration will check the right half of the remaining search space.
            left = mid + 1
    return res


piles = [3, 6, 7, 11]
h = 8
# Output: 4
print(minEatingSpeed(piles, h))
