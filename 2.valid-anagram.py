# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Sorting does take time and space, but good sorting algos can be Averaging O(nlogn), or O(1)
# If both strings are sorted we can just do a compare

def isAnagram(s, t):
    return sorted(s) == sorted(t)
    
s = "cat"
t = "rat"
print(isAnagram(s,t))


# Using dictionary
# time O(s + t), space O(s + t)
# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False

#     countA, countB = {},{}
    
#     for i in range(len(s)):
#         # get method gets the key's value, if the key doesn't exit, return 0 as default
#         # s[i] is the value we want to search, t[i] for countB
#         countA[s[i]] = countA.get(s[i], 0) + 1
#         countB[t[i]] = countB.get(t[i], 0) + 1

#     for v in countA: 
#         # using get so no key error if the key doesn't exist
#         if countA[v] != countB.get(v, 0):
#             return False
#     return True

# My original solution
# make string into array, sort both array, compare letters
# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False

#     listA = [s for s in s]
#     listB = [s for s in t]

#     listA.sort()
#     listB.sort()
    
#     for i in range(0, len(listA)):
#         if listA[i] != listB[i]:
#             return False
#     return True
