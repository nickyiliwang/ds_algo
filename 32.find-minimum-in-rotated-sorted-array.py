# Draw solution if confused
# [3,4,5,1,2] => part A: [3,4,5] part B: [1,2]
# if m = 5, left = 3, right = 2
# mid > right means for sure the min number is right
# O(log n)


def findMin(nums):
    left, right = 0, len(nums) - 1
    res = nums[0]

    while left <= right:
        mid = (left + right) // 2
        res = min(res, nums[mid])

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return res

# # Solution 2
# def findMin(nums):
#     res = nums[0]
#     left, right = 0, len(nums) - 1

#     while left <= right:
#         # left most number is smaller than right most number
#         # sorted list no pivot
#         if nums[left] < nums[right]:
#             res = min(res, nums[left])
#             break

#         # we are not touching the right pointer
#         middle = (left + right) // 2
#         res = min(res, nums[middle])
#         # important part
#         # mid point will always bigger or equal to left
#         # this algo is efficient because we are cutting in half in every operation
#         if nums[left] <= nums[middle]:
#             left = middle + 1
#         else:
#             right = middle - 1
#     return res

# # O(n) solution
# def findMin(nums: List[int]) -> int:
#     left, right = 0, len(nums) - 1
#     # no pivot
#     if nums[left] < nums[right]:
#         return nums[left]
#     # if there is pivot
#     # the left number will reach a point where
#     # it's not bigger than the right more number
#     # we don't touch right pointer
#     while nums[left] > nums[right]:
#         left = left + 1
#     return nums[left]

# nums = [3, 4, 5, 1, 2]
# # Output: 11
# findMin(nums)
