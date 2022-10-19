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
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged = []

    def addSecondList(list, n):
        left, right = 0, len(list) - 1

        while left <= right:
            middle = (left + right) // 2
            if list[middle] <= n:
                list.insert(middle + 1, n)
                left = middle + 1
            else:
                right = middle - 1

    if (nums1[0] < nums2[0]):
        merged = nums1
        for n in nums2:
            addSecondList(merged, n)
    else:
        merged = nums2
        for n in nums1:
            addSecondList(merged, n)

    left, right = 0, len(merged) - 1

    print("merged", merged)
    if (len(merged) % 2 == 0):
        leftPart = (left + right) // 2
        rightPart = leftPart + 1

        return (leftPart + rightPart) / 2
    else:
        middle = (left + right) // 2
        return round(merged[middle], 5)


nums1 = [1, 2]
nums2 = [3, 4]

print(
    findMedianSortedArrays(nums1, nums2)
)