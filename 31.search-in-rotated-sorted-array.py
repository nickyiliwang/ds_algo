def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[left] <= nums[mid]:
            # trap it: [4,5,6,7], 4 <= 5 <= 7
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # right sorted portion
        else:
            # trap it: [0,1,2], 0 <= 1 <= 2
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(search(nums, target))

# # using pivots
# # DOES NOT WORK, BUGS WHEN RUNNING [1,3]
# def search(nums: List[int], target: int) -> int:
#     left, right = 0, len(nums) - 1
#     pivotPoint = (left + right) // 2

#     def binarySearch(l, r, t):
#         while l <= r:
#             m = (l+r)//2
#             if (nums[m] == t):
#                 return m
#             elif (nums[m] < t):
#                 l = m + 1
#             else:
#                 r = m - 1
#         return -1

#     while nums[left] > nums[pivotPoint]:
#         pivotPoint = pivotPoint - 1

#     if target == nums[pivotPoint]:
#         return pivotPoint
#     elif target > nums[left]:
#         return binarySearch(left, pivotPoint, target)
#     else:
#         return binarySearch(pivotPoint, right, target)

# nums = [1]
# target = 1

# print(search(nums, target))

# My old solution, not BigO(log n)
# def search(nums: List[int], target: int) -> int:
#     def binarySearch(l, r, t):
#         while l <= r:
#             m = (l+r)//2
#             if (nums[m] == t):
#                 return m
#             elif (nums[m] < t):
#                 l = m + 1
#             else:
#                 r = m - 1
#         return -1

#     left, right = 0, len(nums) - 1

#     # left sorted quadrant, we can ignore right
#     while nums[left] > nums[right]:
#         right = right - 1
#     leftPart = binarySearch(left, right, target)

#     # reset pointers
#     left, right = 0, len(nums) - 1

#     # right quadrant, we can ignore left
#     while nums[left] > nums[right]:
#         left = left + 1
#     rightPart = binarySearch(left, right, target)

#     res = max(leftPart, rightPart)
#     print(res)
#     return res
