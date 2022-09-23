# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


# we want the len of the window - max repeating number <= k
# during any window we want to
# Shit day for learning, gonna just study the answer

def characterReplacement(s, k):
    # to count the repeating numbers
    counter = {}
    # window
    left = 0
    res = 0
    for right in range(len(s)):
        counter[s[right]] = 1 + counter.get(s[right], 0)

        while (right - left + 1) - max(counter.values()) > k:
            counter[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


s = "AABABBA"
k = 1
characterReplacement(s, k)

# # we want the len of the window - max repeating number <= k
# # during any window we want to
# # WIP my solution

# def characterReplacement(s, k):
#     # to count the repeating numbers
#     counter = {}
#     # window
#     left, right = 0, 0
#     res = 0

#     counter[s[left]] = counter.get(s[0], 1)

#     # while right window is less than string length, and left pointer is not over right pointer
#     while right < len(s) - 1:
#         maxCurrentChar = max(counter.values())
#         windowLen = right - left
#         res = max(res, windowLen)
#         if windowLen - maxCurrentChar <= k:
#             right += 1
#             counter[s[right]] = counter.get(s[right], 0) + 1
#         else:
#             left += 1
#             counter[s[left]] = counter.get(s[left], 0) + 1

#     print(res)
#     return res


# s = "AABABBA"
# k = 1
# characterReplacement(s, k)

# for right in range(len(s)):

# KeyError, and string index out of range
# while right < len(s):
#     right += 1
#     if s[right] in counter:
#         counter[s[right]] = counter[s[right]] + 1
#     else:
#         counter[s[right]] = counter.get(counter[s[right]], 0) + 1
