# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# time: O(n), space: O(n)
# sliding window approach
def lengthOfLongestSubstring(s):
    # validates unique strings
    validator = set()
    left = 0
    res = 0

    # right variable will constantly moving right
    for right in s:
        # if the right char is in validator set
        while right in validator:
            # remove the very first element which is the repeating char
            validator.remove(s[left])
            # increment left pointer
            left += 1
        # keep adding the right character and update the result with the bigger number
        # comparing current result and current length of the validator set
        validator.add(right)
        res = max(res, len(validator))

    print(res)
    return res


s = "dvdf"
lengthOfLongestSubstring(s)


# I had to do this to understand that sliding window is really the better solution
# def lengthOfLongestSubstring(s):
#     validator = set()
#     res = 0
#     temp = 0

#     for c in s:
#         if c in validator:
#             print(len(validator))
#             res = max(res, temp)
#             validator.clear()
#             validator.add(c)
#             temp = 1

#         else:
#             temp += 1
#             validator.add(c)
#             res = max(res, temp)

#     print(res)
#     return res


# s = "dvdf"
# lengthOfLongestSubstring(s)
