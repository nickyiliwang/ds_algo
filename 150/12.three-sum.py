def threeSum(nums):
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            threeSum = n + nums[left] + nums[right]
            if threeSum < 0:
                left -= 1
            elif threeSum > 0:
                right += 1

            else:
                res.append([n, nums[left], nums[right]])
                left += 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res


# Time nested loop + sorting =  nest loop worst time
# Time O(n ^ 2) + O(nlogn) =  O(n ^ 2)

# Space: O(1), O(n) depends on sorting implementation

# Keys:
# Sort the array
# Make sure no duplicates during loop: i > 0 and n == nums[i - 1]
# Left starts at the second number (index 1)
# Do the two pointer sort
#


def threeSum(nums):
    res = []

    # with a sorted array we can then use pointers
    nums.sort()

    if len(nums) < 3:
        return []

    for i, n in enumerate(nums):
        # if index is bigger than 0 and index value (ie. nums[0] == nums[1]) is a duplicate
        # go next iteration
        if i > 0 and n == nums[i - 1]:
            print("go next", i, n, nums[i - 1])
            continue

        # using pointers
        # moving left and right pointers like two sum
        # but we calculate the sum of 3 numbers
        # left pointer will always be current index + 1
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = n + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1

            else:
                # found pair, appending to res
                res.append([n, nums[l], nums[r]])
                # Remember to increment by one after the result is appended
                l += 1

                # while current left pointer is the same as the previous left pointer value
                # left index does not meet right index
                # increment it
                # ** Why do we not do the same for the right pointer ?
                # Because we only need to check left, if the right point is too large twice, our previous if statement will adjust it, ie. [1,2,3,5,5], it's just gonna move right pointer left twice if sum is bigger than 0
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                # [-2, -2, 0, 0, 2, 2]
    return res


nums = [-1, 0, 1, 2, -1, -4, -4]
# Output: [[-1,-1,2],[-1,0,1]]

threeSum(nums)

# def threeSum(nums):
#     res = []
#     nums.sort()
#     if (len(nums) < 3):
#         return []

#     base = nums[0]
#     l, r = 1, len(nums) - 1

#     while l < r:
#         print([base, nums[l], nums[r]])
#         while nums[r] == base:
#             r -= 1

#         while nums[l] == base:
#             l += 1

#         currSum = base + nums[l] + nums[r]

#         if currSum == 0:
#             return [base, nums[l], nums[r]]

#         elif currSum > 0:
#             r -= 1

#         elif currSum < 0:
#             l += 1

#         else:
#             return []

# nums = [-1, 0, 1, 2, -1, -4]
# # Output: [[-1,-1,2],[-1,0,1]]

# threeSum(nums)

# def threeSum(nums):
#     if (len(nums) < 3):
#         return []

#     i = 0

#     while i < len(nums) - 2:
#         j = i + 1
#         k = j + 1
#         # print(nums[i], nums[i + 1], nums[i + 2])

#         # if (nums[i] != nums[j], nums[j] != nums[k], nums[i] != nums[k]):
#         print(nums[i], nums[j], nums[k])
#         i += 1

#     # for i, n in enumerate(nums):
#     #     print(i, n)

# nums = [-1, 0, 1, 2, -1, -4]
# threeSum(nums)
