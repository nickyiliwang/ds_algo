# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

def longestConsecutive(nums):



# # from counting the max number in the array
# # maybe there was some way to do one pass to the largest number range
# # have a sequential counter that increments
# # need a hashmap then

# #  this does not take into account
# # this solution does not take into account of negative numbers
# # during the loop, we are checking each number against the dictionary
# # starting from 0 we are looking for continuous sequences
# # if we find a sequence + 1 to seq var, the result var will take the value of seq
# # if j and i are 0's, we use the dictionary to look for how many times the j is repeated

# # this solution keeps failing tests haha

# def longestConsecutive(nums):
#     res = 0
#     map = {}
#     max = int()

#     # *in* seems like an O(n)
#     # if 1 in nums:
#     #     print('found 1')

#     for n in nums:
#         if n > max:
#             max = n
#         map[n] = 1

#     print(map)

#     seq = 0
#     j = 0
#     for i in range(max + 1):  # + 1 to get the full range, ie. 0 - 199 + 1 = 200
#         if (map.get(i) != None):
#             if (j + i == 0):
#                 seq += map[j]

#             elif (j + 1 == i):
#                 seq += map[i]

#         else:
#             if (seq >= res):
#                 res = seq
#             seq = 0

#         if (seq >= res):
#             res = seq
#         j = i

#     print(res)
#     return res


# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# 9
# nums = [100, 4, 200, 1, 3, 2]
# 4
nums = [0, -1]
# 2
longestConsecutive(nums)
