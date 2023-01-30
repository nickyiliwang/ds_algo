def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left <= right:
        currSum = numbers[left] + numbers[right]

        if currSum < target:
            left += 1
        elif currSum > target:
            right -= 1
        else:
            return [left + 1, right + 1] 


# Time: O(n) Space: O(1)
# Because of sorted array we can do this
# if current sum is bigger than target, move the right pointer to the left to decrease the sum
# else if current sum is smaller than target, move left point to the right to increase the sum
# return index of correct number combo
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1

        elif curSum < target:
            l += 1

        else:
            # added by one as an integer array [index1, index2] of length 2
            return [l + 1, r + 1]


numbers = [2, 7, 11, 15]
target = 9

print(twoSum(numbers, target))
