from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 - 2

        if len(A) > len(B):
            A, B = nums2, nums1

        left, right = 0, len(A) - 1
        while True:
            A_Mid = (left + right) // 2
            B_Mid = half - A_Mid

            A_Left = A[A_Mid] if A_Mid >= 0 else float("-inf")
            A_Right = A[A_Mid + 1] if A_Mid < len(A) - 1 else float("inf")

            B_Left = B[B_Mid] if B_Mid >= 0 else float("-inf")
            B_Right = B[B_Mid + 1] if B_Mid < len(B) - 1 else float("inf")

            if A_Left <= B_Right and B_Left <= A_Right:
                if total % 2 == 0:
                    return (max(A_Left, B_Left) + min(A_Right, B_Right)) / 2
                else:
                    return min(A_Right, B_Right)
            elif A_Left > B_Right:
                right = A_Mid - 1
            else:
                left = A_Mid + 1


nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 4, 5, 5, 6, 7, 8]

print(Solution.findMedianSortedArrays("", nums1, nums2))

# Time: O(log(min(m, n)))
# Space: O(n)
# using partitions:
# A: [1,2,3]
# B: [1,2,3] [4,5,6,7,8]
# Binary search to find the median


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 - 2

        if len(A) > len(B):
            A, B = nums2, nums1

        left, right = 0, len(A) - 1
        while True:
            A_Mid = (left + right) // 2
            B_Mid = half - A_Mid

            # ALeft -inf [{Left can be out}Mid{Right can be out of bound}] +inf A_Right
            A_Left = A[A_Mid] if A_Mid >= 0 else float("-inf")
            A_Right = A[A_Mid + 1] if A_Mid < len(A) - 1 else float("inf")

            B_Left = B[B_Mid] if B_Mid >= 0 else float("-inf")
            B_Right = B[B_Mid + 1] if B_Mid < len(B) - 1 else float("inf")

            if A_Left <= B_Right and B_Left <= A_Right:
                # Even
                if total % 2 == 0:
                    # [{1,2,[3]},{[4]}]
                    # [{1,2,[3]},{[4],5,6,7}]
                    # max(3, 3) + min(4,4)
                    return (max(A_Left, B_Left) + min(A_Right, B_Right)) / 2
                # Odd
                else:
                    return min(A_Right, B_Right)
            # [{1,2,3,4}] A_left = 4
            # [{1,2},{3,4,5,6,7}] B_right = 3
            #  A_left(4) cannot be bigger than B_right(3)
            # Partition is wrong
            elif A_Left > B_Right:
                right = A_Mid - 1
            else:
                left = A_Mid + 1


# Divide-and-conquer approach.
# The function takes in two input lists nums1 and nums2 and returns a float as the median. The function first assigns the shorter of the two input lists to a variable A and the longer one to a variable B.
# It then calculates the Mid index of the combined list by taking the floor division of the total number of elements in the two lists by 2.
# It then enters a while loop. Within the loop, it finds the Mid index of both lists A and B and assigns them to A_Mid and B_Mid respectively.
# It then checks if the element at the Mid index of A is less than or equal to the element immediately following the Mid index of B, and if the element at the Mid index of B is less than or equal to the element immediately following the Mid index of A.
# If this is true, it checks if the total number of elements in the two lists is even or odd. If it's even, it returns the average of the largest element of the two Mid elements of the two arrays and the smallest element of the two Mid elements of the two arrays as the median. If it's odd, it returns the smaller element of the two Mid elements of the two arrays as the median.
# If it's not true, it checks if the element at the Mid index of A is greater than the element immediately following the Mid index of B. If it is, it moves the right pointer one step to the left, else it moves the left pointer one step to the right.


# def findMedianSortedArrays(nums1, nums2):
#     merged = []

#     def addSecondList(list, n):
#         left, right = 0, len(list) - 1
#         while left <= right:
#             Mid = (left + right) // 2
#             if list[Mid] < n:
#                 if (Mid + 1) < len(list) and list[Mid + 1] > n:
#                     list.insert(Mid + 1, n)
#                     return
#                 elif (Mid + 1) == len(list):
#                     list.insert(Mid + 1, n)
#                     return
#                 left = Mid + 1

#             elif list[Mid] == n:
#                 list.insert(Mid + 1, n)
#                 left = Mid + 1
#                 return
#             else:
#                 right = Mid - 1

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
#         Mid = (left + right) // 2
#         return merged[Mid]

# nums1 = [1, 2]
# nums2 = [3, 4]

# print(
#     findMedianSortedArrays(nums1, nums2)
# )

# The time complexity of this function is O(n log n) because it combines two sorted arrays by inserting elements of the second array one by one into the first array using a binary search algorithm, which has a time complexity of O(log n). This binary search operation is performed n times, once for each element in the second array, resulting in a total time complexity of O(n log n).

# The space complexity of this function is O(n) because it creates a new array, merged, which has a maximum size of n, where n is the total number of elements in the two input arrays.


# Brute Force
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         merged = nums1 + nums2
#         merged.sort()

#         total = len(merged) - 1
#         mid = total // 2
#         if (total % 2 == 1):
#             return merged[mid]
#         else:
#             return (merged[mid] + (merged[mid] - 1)) / 2
