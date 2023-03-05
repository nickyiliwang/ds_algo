from typing import *
import os
os.system('clear')

# looking at it in reverse
# array only has positive numbers
# new max = max(old max, curr iteration num)
# old max is the right pointer max


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        oldMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(oldMax, arr[i])
            arr[i] = oldMax
            oldMax = newMax
        print(arr)
        return arr

# for looping arr in reverse
#   newMax(-1) = max(1, -1)
#   arr[5] = -1
#   oldMax(-1) = newMax(-1)

Solution.replaceElements(0, [17, 18, 5, 4, 6, 1])


# idea: get the largest number in the array and get the index, all previous numbers will be this number, then do it again until last item


# # Time Limit Exceeded
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         if not arr:
#             return []

#         for i in range(len(arr)):
#             if len(arr[i+ 1:]) > 0:
#                 arr[i] = max(arr[i+ 1:])
#             elif i + 1 < len(arr):
#                 arr[i] = arr[i + 1]

#         arr[-1] = -1
#         print(arr)
#         return arr


# Solution.replaceElements(0, [57010, 40840, 69871, 14425, 70605])
