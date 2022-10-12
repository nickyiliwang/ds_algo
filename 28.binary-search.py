# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

def search(nums, target):
    # default return -1
    res = -1
    # left and right pointers
    left = 0
    right = len(nums) - 1

    # while left is before right
    # or if they are equal, meaning either the number of items are 1
    while left <= right:
        # get the mid pointer
        # (l + r) // 2 can lead to overflow
        middle = left + ((right - left) // 2)
        # return the index of correct number
        if (nums[middle] == target):
            res = middle
        # if the number is smaller than the target
        # we ove left pointer up
        if (nums[middle] < target):
            left = middle + 1
        # number is too large
        # move the right pointer down
        else:
            right = middle - 1

    print(res)
    return res


nums = [1,2,3,4,5]
target = 5

search(nums, target)
