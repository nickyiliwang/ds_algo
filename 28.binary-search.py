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

    return res


nums = [1,2,3,4,5]
target = 5

search(nums, target)
