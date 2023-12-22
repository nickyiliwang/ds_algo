from typing import *


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # List Comprehension
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        print(stack)
        return len(stack)


print(Solution.carFleet("", 10, [0, 4, 2], [2, 1, 3]))  # output 3


# Explanation
# sorted(pair)
# We need to sort the pairs before stacking

# (target - position) / speed = time to position at constant speed.

# stack[-1] <= stack[-2]
# We always want to pop the slower one
