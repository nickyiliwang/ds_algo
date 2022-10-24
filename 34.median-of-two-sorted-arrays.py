# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List

# did not know that both sorted arrays can be unsorted when combined
# [1,3]
# [2]

# BigO:
# Time: O(log (m + n)) ?
# Space: O(m + n)


# def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
#     merged = []

#     def addSecondList(list, n):
#         left, right = 0, len(list) - 1
#         while left <= right:
#             middle = (left + right) // 2
#             if list[middle] < n:
#                 if (middle + 1) < len(list) and list[middle + 1] > n:
#                     list.insert(middle + 1, n)
#                     left = middle + 1
#                     return
#                 elif (middle + 1) == len(list):
#                     list.insert(middle+1, n)
#                     left = middle + 1
#                     return
#                 else:
#                     left = middle + 1

#             elif list[middle] == n:
#                 list.insert(middle + 1, n)
#                 left = middle + 1
#                 return
#             else:
#                 right = middle - 1

#     # compare initial list

#     if (len(nums1) == 0 or len(nums2) == 0):
#         merged = nums1 + nums2
#     elif (nums1[0] <= nums2[0]):
#         merged = nums1
#         for n in nums2:
#             addSecondList(merged, n)

#     else:
#         merged = nums2
#         for n in nums1:
#             addSecondList(merged, n)

#     print("merged", merged)
#     # get median
#     if (len(merged) % 2 == 0):

#         left, right = 0, len(merged) - 1

#         leftPart = (left + right) // 2
#         rightPart = leftPart + 1

#         return (merged[leftPart] + merged[rightPart]) / 2
#     else:
#         left, right = 0, len(merged) - 1
#         middle = (left + right) // 2
#         return merged[middle]


# nums1 = [1, 2]
# nums2 = [3, 4]

# print(
#     findMedianSortedArrays(nums1, nums2)
# )

# O(log(m + n))
# using partitions:
# A: [1,2,3]
# B: [1,2,3] [4,5,6,7,8]
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # always want the shorter array as A
    if len(B) < len(A):
        A, B = B, nums1

    left, right = 0, len(A) - 1
    while True:
        middleA = (left+right) // 2
        middleB = half - middleA - 2  # both A and B starts at index 0, this removes off by 1

        Aleft = A[middleA] if middleA >= 0 else float("-infinity")  # middleA < than 0
        Aright = A[middleA + 1] if (middleA+1) < len(A) else float("infinity") # out of bounds
        Bleft = B[middleB] if middleB >= 0 else float("-infinity")
        Bright = B[middleB + 1] if (middleB+1) < len(B) else float("infinity") # out of bounds

        if Aleft <= Bright and Bleft <= Aright:
            # even
            if total % 2 == 0:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # odd
            return min(Aright, Bright)
        elif Aleft > Bright:
            right = middleA - 1
        else:
            left = middleA + 1

nums1 = [1, 2]
nums2 = [3, 4]

print(
    findMedianSortedArrays(nums1, nums2)
)
