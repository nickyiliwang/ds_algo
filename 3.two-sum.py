def twoSum(nums, target):
    # we can do this in one pass
    prevMap = {}  # val: index
    # enumerate gives the index and value of an iterative data structure
    for i, n in enumerate(nums):
        diff = target - n
        # x in dict
        # meaning we got a difference
        if diff in prevMap:
            # return the index of the diff and the current index of the loop
            return [prevMap[diff], i]
        # make sure to update the map with the current number as key and index as value
        prevMap[n] = i
    return


twoSum([3, 3, 2, 1], 6)

# def twoSum(nums, target):
# # My solution with hashMap and cal for diff
# # O(n + n), relative complexity of O(n)
#     res = []
#     hashMap = {}
#     # get the hashMap
#     for x in range(len(nums)):
#         # key: number, value: index in arr
#         hashMap[nums[x]] = x

#     for x in range(len(nums)):
#         # 6 - 3 = 3
#         diff = target - nums[x]
#         # key in the hasMap check if the diff exist O(1), returns 1 or None
#         key = hashMap.get(diff)
#         # the key exist and the key index isn't the index of x (itself), we have a diff
#         if (key and hashMap[diff] != x):
#             res = [hashMap[diff],  x]

#     print(res)
#     return res

# brute force
# With nested loops, O(n^2)
# Output Limit Exceeded
# def twoSum(nums, target):
#     res = []
#     for x in range(len(nums)):
#         y = x + 1
#         while y <= len(nums) - 1:
#             print(nums[x] + nums[y])
#             if (nums[x] + nums[y] == target):
#                 res = [x, y]
#             y += 1

#     print(res)
#     return res
