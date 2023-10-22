# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

from typing import * 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if (len(arr) > 1):
                mid = len(arr) // 2
                leftArr = arr[:mid]
                rightArr = arr[mid:]
                    
                mergeSort(leftArr)
                mergeSort(rightArr)
                
                # merging 
                leftIdx = 0
                rightIdx = 0
                mergedIdx = 0
                    
                # Loop till one or both arr is empty
                while leftIdx < len(leftArr) and rightIdx < len(rightArr):
                    if (leftArr[leftIdx] < rightArr[rightIdx]):
                        arr[mergedIdx] = leftArr[leftIdx]
                        leftIdx += 1
                    else:
                        arr[mergedIdx] = rightArr[rightIdx]
                        rightIdx +=1
                        
                    mergedIdx += 1
                    
                while leftIdx < len(leftArr):
                    arr[mergedIdx] = leftArr[leftIdx]
                    leftIdx += 1
                    mergedIdx += 1
                
                while rightIdx < len(rightArr):
                    arr[mergedIdx] = rightArr[rightIdx]
                    rightIdx += 1
                    mergedIdx += 1
                    
            return arr
    
        return mergeSort(nums)
                
                
        
print(Solution.sortArray("", [0]))


# mergeSort(arr)
#     if length of arr is less than or equal to 1
#         return arr
        
#     mid = length of arr divided by 2
#     leftArray = mergeSort(first half of arr)
#     rightArray = mergeSort(second half of arr)
    
#     return merge(leftArray, rightArray)

# merge(leftArray, rightArray)
#     mergedArray = empty array
    
#     while leftArray and rightArray are not empty
#         if first element of leftArray is less than or equal to first element of rightArray
#             append first element of leftArray to mergedArray
#             remove first element from leftArray
#         else
#             append first element of rightArray to mergedArray
#             remove first element from rightArray
    
#     append remaining elements of leftArray to mergedArray
#     append remaining elements of rightArray to mergedArray
    
#     return mergedArray