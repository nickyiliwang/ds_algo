from collections import deque


def solution(temperatures):
    res = [0] * len(temperatures)
    stack = deque()

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            position = stack.pop()
            res[position] = i - position
        stack.append(i)

    return res


# monotonic decreasing stack: always decreasing or remaining constant, and never increasing
# Time: O(n), Space: O(n)
def solution(temperatures):
    # instantiate all position with default of 0 days
    # going to replace each position with days found
    res = [0] * len(temperatures)
    stack = deque()

    for i, temp in enumerate(temperatures):
        # Only when we find a higher temperature than the current highest temperature, then we can start popping every value in the stack and updating the position with the day difference
        while stack and temperatures[stack[-1]] < temp:
            position = stack.pop()
            # update each day's position with the day difference
            res[position] = i - position
        stack.append(i)

    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1,1,4,2,1,1,0,0]
solution(temperatures)

# # blind brute force
# def solution(temperatures):
#     res = []
#     for i, temp in enumerate(temperatures):
#         # we start from the next number to the end of the list
#         startFrom = temperatures[i + 1:len(temperatures)]

#         temporary = []
#         # O(n^2) loop to compare every number
#         for j, d in enumerate(startFrom):
#             # if the next day is higher temp than prev
#             if (d > temp):
#                 # append all temperature position higher than i
#                 # j + 1 is the next number since i
#                 temporary.append(j + 1)
#         if temporary:
#             # we only want the first number
#             res.append(temporary[0])
#         else:
#             # nothing found, append 0
#             res.append(0)
#     print(res)
#     return res

# Attempt May 17th 2023
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         if not temperatures:
#             return []

#         res = []
#         for i, temp in enumerate(temperatures):
#             left = i
#             right = i + 1
#             while right < len(temperatures):
#                 if temperatures[left] < temperatures[right]:
#                     right - left
#                     break
#                 right += 1
