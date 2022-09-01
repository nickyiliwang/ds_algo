# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# My solution
def topKFrequent(nums, k):
    hashMap = {}
    # build a hashMap with:
    # value:
    for n in nums:
        hashMap[n] = hashMap.get(n, 0) + 1

    # gets the (key, val) pair in a tuple
    items = hashMap.items()

    # sorting by the second tuple which was the times repeated, in reverse order
    sortedItems = sorted(items, key=lambda tup: tup[1], reverse=True)

    # only take the first index in the tuple, the key, in the sortedItems tuple list, only go up to k index
    return [s[0] for s in sortedItems[:k]]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
