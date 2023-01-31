def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2 - 2

    if len(A) > len(B):
        A, B = nums2, nums1

    left, right = 0, len(A) - 1
    while True:
        A_Middle = (left + right) // 2
        B_Middle = half - A_Middle

        A_Left = A[A_Middle] if A_Middle >= 0 else float("-infinity")
        A_Right = A[A_Middle + 1] if A_Middle < len(A) - 1 else float("infinity")

        B_Left = B[B_Middle] if B_Middle >= 0 else float("-infinity")
        B_Right = B[B_Middle + 1] if B_Middle < len(B) - 1 else float("infinity")

        if A_Left <= B_Right and B_Left <= A_Right:
            if total % 2 == 0:
                return (max(A_Left, B_Left) + min(A_Right, B_Right)) / 2
            return min(A_Right, B_Right)
        elif A_Left > B_Right:
            right = A_Middle - 1
        else:
            left = A_Middle + 1


# O(log(m + n))
# using partitions:
# A: [1,2,3]
# B: [1,2,3] [4,5,6,7,8]
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    # Since "half" is derived from length, we -2 to fix off by one
    half = total // 2 - 2

    # A will always be shorter array
    if len(A) > len(B):
        A, B = nums2, nums1

    left, right = 0, len(A) - 1
    while True:
        A_Middle = (left + right) // 2
        # getting the left partition of B
        B_Middle = half - A_Middle

        A_Left = A[A_Middle] if A_Middle >= 0 else float("-infinity")
        A_Right = A[A_Middle + 1] if A_Middle < len(A) - 1 else float("infinity")

        B_Left = B[B_Middle] if B_Middle >= 0 else float("-infinity")
        B_Right = B[B_Middle + 1] if B_Middle < len(B) - 1 else float("infinity")

        # Check partitions
        if A_Left <= B_Right and B_Left <= A_Right:
            # even
            if total % 2 == 0:
                return (max(A_Left, B_Left) + min(A_Right, B_Right)) / 2
            # odd
            return min(A_Right, B_Right)
        elif A_Left > B_Right:
            right = A_Middle - 1
        else:
            left = A_Middle + 1


nums1 = [1, 2]
nums2 = [3, 4]

print(findMedianSortedArrays(nums1, nums2))

# Divide-and-conquer approach.
# The function takes in two input lists nums1 and nums2 and returns a float as the median. The function first assigns the shorter of the two input lists to a variable A and the longer one to a variable B.
# It then calculates the middle index of the combined list by taking the floor division of the total number of elements in the two lists by 2.
# It then enters a while loop. Within the loop, it finds the middle index of both lists A and B and assigns them to A_Middle and B_Middle respectively.
# It then checks if the element at the middle index of A is less than or equal to the element immediately following the middle index of B, and if the element at the middle index of B is less than or equal to the element immediately following the middle index of A.
# If this is true, it checks if the total number of elements in the two lists is even or odd. If it's even, it returns the average of the largest element of the two middle elements of the two arrays and the smallest element of the two middle elements of the two arrays as the median. If it's odd, it returns the smaller element of the two middle elements of the two arrays as the median.
# If it's not true, it checks if the element at the middle index of A is greater than the element immediately following the middle index of B. If it is, it moves the right pointer one step to the left, else it moves the left pointer one step to the right.


# def findMedianSortedArrays(nums1, nums2):
#     merged = []

#     def addSecondList(list, n):
#         left, right = 0, len(list) - 1
#         while left <= right:
#             middle = (left + right) // 2
#             if list[middle] < n:
#                 if (middle + 1) < len(list) and list[middle + 1] > n:
#                     list.insert(middle + 1, n)
#                     return
#                 elif (middle + 1) == len(list):
#                     list.insert(middle + 1, n)
#                     return
#                 left = middle + 1

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

# The time complexity of this function is O(n log n) because it combines two sorted arrays by inserting elements of the second array one by one into the first array using a binary search algorithm, which has a time complexity of O(log n). This binary search operation is performed n times, once for each element in the second array, resulting in a total time complexity of O(n log n).

# The space complexity of this function is O(n) because it creates a new array, merged, which has a maximum size of n, where n is the total number of elements in the two input arrays.
