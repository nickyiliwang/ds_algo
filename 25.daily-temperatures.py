# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# stack solution
# monotonic decreasing stack: always decreasing or remaining constant, and never increasing
# Time: O(n), Space: O(n)
def solution(temperatures):
    # instantiate all position with default of 0 days
    # going to replace each position with days found
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        # while the stack isn't empty
        # and our current day temperature is higher than previous days
        # temperatures[stack[-1]] is getting value from the top of the stack and the temperature value
        # we are only storing the index and because we can reference the value from the temperatures list 
        while stack and t > temperatures[stack[-1]]:
            stackIndex = stack.pop()
            # ok we found the temperature
            # i - the index to get the days difference
            res[stackIndex] = i - stackIndex
        # keep appending days index for the next loop
        stack.append(i)

    print(res)
    return res

# # blind brute force
# def solution(temperatures):
#     res = []
#     for i, t in enumerate(temperatures):
#         # we start from the next number to the end of the list
#         startFrom = temperatures[i + 1:len(temperatures)]

#         temporary = []
#         # O(n^2) loop to compare every number
#         for j, d in enumerate(startFrom):
#             # if the next day is higher temp than prev
#             if (d > t):
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


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1,1,4,2,1,1,0,0]
solution(temperatures)
