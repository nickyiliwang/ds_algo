def containsDuplicate(nums):
    hashSet = set()
    for n in nums:
        if n in hashSet:
            return True
        else:
            hashSet.add(n)
    return False


test = [0, 4, 5, 0, 3, 6]
print(containsDuplicate(test))

# Time Limit Exceeded Error solution
#
# def containsDuplicate(nums):
#     dict = {}
#     res = False
#     for i in range(0, len(nums)):
#         val = nums[i]
#         print(val)
#         if val in dict:
#             res = True
#         else:
#             dict.val = 0
#         print(dict)
#     return res

# Answer:
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashSet = set()

#         for n in nums:
#             if n in hashSet:
#                 return True
#             hashSet.add(n)
#         return False

# hashmap/hashtable/dictionary/js object
# key/pair value uses more space/memory but helps with time complexity

# hashSet/set()
# hash set is different than hashtable
# var = {"Geeks", "for", "Geeks"}
# type(var) OUTPUT: set

# sorting
# if the array is sorted any dup is next to each other
# n(log)

# terms: O(nlogn)
# O(nlogn) is known as loglinear complexity.
# logn operations will occur n times.
# O(nlogn) time is common in recursive sorting algorithms.
# sorting algorithms using a binary tree sort and most other types of sorts.

# bad
# brute force is O(n^2) nested loop
