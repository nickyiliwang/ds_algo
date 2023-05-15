from collections import Counter


def checkInclusion(s1, s2):
    need, have = Counter(s1), Counter()
    window = len(s1)

    for i in range(len(s2)):
        if i < window:
            have[s2[i]] += 1
        else:
            have[s2[i - window]] -= 1
            have[s2[i]] += 1

        if need == have:
            return True

    return False

# Explanation
# Key: c2[s2[i - window]] -= 1
# current index - window length will result in the left pointer index


# # alternative solution that doesn't require the initial loops
# # s2 will start with the length of s1, which is initial window
# def checkInclusion(s1, s2):
#     if len(s1) > len(s2):
#         return False

#     c1 = Counter(s1)
#     window = len(s1)

#     c2 = Counter(s2[:window])

#     if c1 == c2:
#         return True

#     for i in range(len(s2)):
#         # Gets the left most val to - 1 to counter
#         c2[s2[i]] -= 1

#         if i < len(s2) - window:
#             # Then add a new char from s2
#             c2[s2[i + window]] += 1

#         if c1 == c2:
#             return True

#     return False


# s1 = "ba"
# s2 = "eidbaooo"

# print(checkInclusion(s1, s2))

# def checkInclusion(s1, s2):
#     # target(s1) cannot be longer than query(s2)
#     if len(s1) > len(s2):
#         return False

#     s1Count, s2Count = [0] * 26, [0] * 26

#     for i in range(len(s1)):
#         # print(ord(s1[i]), ord('a'))
#         # a = 97, a = 97
#         # b = 98, a = 97
#         # c = 99, a = 97
#         # the diff are the indexes, and we increment them by one
#         s1Count[ord(s1[i]) - ord('a')] += 1
#         s2Count[ord(s2[i]) - ord('a')] += 1

#     # instantiate matches for final result
#     # we only have perfect matches when all 26 alphabet matches
#     matches = 0
#     for i in range(26):
#         if s1Count[i] == s2Count[i]:
#             matches += 1
#     l = 0

#     for r in range(len(s1), len(s2)):
#         if (matches == 26):
#             return True

#         index = ord(s2[r]) - ord('a')
#         s2Count[index] += 1
#         if (s2Count[index] == s1Count[index]):
#             matches += 1

#         # checking if the alphabets were equal and we made it too large
#         # maybe we do this because we are not counting repeating numbers
#         # ie. s1Count[0] = 1 and s2Count[0] = 2
#         # ie. s1Count[0] = 2 and s2Count[0] = 2 matches
#         # matches - 1 fix it
#         elif (s1Count[index] + 1 == s2Count[index]):
#             matches -= 1

#         index = ord(s2[l]) - ord('a')
#         s2Count[index] -= 1
#         if (s2Count[index] == s1Count[index]):
#             matches += 1
#         # under provisioned maybe
#         elif (s1Count[index] - 1 == s2Count[index]):
#             matches -= 1

#         l += 1

#     res = (matches == 26)

#     return res

# s1 = "abc"
# s2 = "ababcd"

# checkInclusion(s1, s2)

# How is Counter different than a python hashtable ?
# collections.Counter is a Python built-in class that is a subclass of dict. It is designed specifically for counting items in a collection, such as a list or a string.

# One of the main differences between Counter and a regular Python dict is that Counter has a default value of zero for keys that do not exist in the dictionary. This means that if you try to access a key that is not in the Counter object, it will return zero instead of raising a KeyError. This can be useful when counting items in a collection, as it allows you to easily count items that may not exist in the collection.

# Additionally, Counter has several convenient methods for counting items, such as most_common() which returns a list of the n most common elements and their counts.

# dict is a general-purpose hashtable implementation in python, it is a key-value store that can be used for storing any kind of data, where keys have to be unique, and it returns an error when trying to access non existent keys, whereas Counter is mainly used for counting items in a collection and has a default value of zero, it is more efficient when doing counting operations.

# # Attempt 2
# # hashmap
# # not a working solution.

# import string

# def checkInclusion(s1, s2):
#     res = False
#     s1hash = dict.fromkeys(string.ascii_lowercase, 0)
#     s2hash = dict.fromkeys(string.ascii_lowercase, 0)

#     for c in s1:
#         s1hash[c] = s1hash.get(c, 0) + 1

#     for i in range(len(s1)):
#         s2hash[s2[i]] = s2hash.get(s2[i], 0) + 1

#     print(s2hash)
#     l = 0
#     k = len(s1)
#     while k < len(s2):
#         s2hash[s2[k]] = s2hash.get(s2[k], 0) + 1
#         s2hash[s2[l]] -= 1
#         if s1hash == s2hash:
#             res = True

#         k += 1
#         l += 1

#     print(res)
#     return res

# s1 = "a"
# s2 = "ab"

# checkInclusion(s1, s2)

# # Attempt 1
# # blind
# # idea was to loop back and forth comparing the window with s1
# # print result

# def checkInclusion(s1, s2):
#     res = False
#     k = len(s1)
#     for i in range(len(s2) - 1):
#         # print("forward", s2[i:k + i])
#         if s2[i:k + i] == s1:
#             res = True
#         if i >= k:
#             temp = s2[i - k] + s2[i]
#             print("backward", temp)
#             if temp == s1:
#                 res = True
#     print(res)
#     return res

# s1 = "ab"
# s2 = "eidbaooo"

# checkInclusion(s1, s2)


# attempt may 15th 2023
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         validator = set(s1)
#         count1,  = Counter()
#         left = 0

#         for s in s1:
#             count1[s] += 1

#         for right in range(len(s2)):
#             count2 = Counter()
#             while s2[right] in validator:
#                 left = right

#             while s2[right] in validator:
#                 count2[s2[right]] += 1


#         # for s in s2:
#         #     if s in validator:
#         #         count2[s] += 1

#         #     if count1 == count2:
#         #         return True
#         return False


# print(Solution.checkInclusion("", "ab", "eidbaooo"))
