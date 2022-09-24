# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


# Attempt 3
# sliding window pointers
# Java solution is the same

def checkInclusion(s1, s2):
    # edge case
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26

    for i in range(len(s1)):
        # print(ord(s1[i]), ord('a'))
        # a = 97, a = 97
        # b = 98, a = 97
        # c = 99, a = 97
        # the diff are the indexes, and we increment them by one
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    # print(s1Count)
    # print(s2Count)

    # instantiate matches for final result
    # we only have perfect matches when all 26 alphabet matches
    matches = 0
    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches += 1
    l = 0

    for r in range(len(s1), len(s2)):
        if (matches == 26):
            return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if (s2Count[index] == s1Count[index]):
            print("ran", s1Count, s2Count)
            print("index", index)

            matches += 1
        # checking if the alphabets were equal and we made it too large
        # maybe we do this because we are not counting repeating numbers
        # ie. s1Count[0] = 1 and s2Count[0] = 2
        # ie. s1Count[0] = 2 and s2Count[0] = 2 matches
        # matches - 1 fix it
        elif (s1Count[index] + 1 == s2Count[index]):
            # print("ran", s1Count[index] + 1)
            # print("ran", s2Count[index])
            # print("ran", index)
            print("ran", s1Count, s2Count)
            print("index", index)

            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if (s2Count[index] == s1Count[index]):
            matches += 1
        # under provisioned maybe
        elif (s1Count[index] - 1 == s2Count[index]):
            matches -= 1

        l += 1

    res = (matches == 26)
    print('res')
    return res


s1 = "abc"
s2 = "ababcd"

checkInclusion(s1, s2)

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
