def lengthOfLongestSubstring(s):
    validator = set()
    left = 0
    res = 0

    for right in s:
        while right in validator:
            validator.remove(s[left])
            left += 1
        validator.add(right)
        res = max(res, len(validator))

    return res


# Time: O(n), Space: O(n)
# sliding window
def lengthOfLongestSubstring(s):
    # validates unique strings
    validator = set()
    left = 0
    res = 0

    # right variable will constantly moving right
    for right in s:
        # if the right char is in validator set
        # *** important ***
        # say is the window is [a, b, c] and the next chat is b
        # this while loop and left += 1 will keep running and remove "a" and "b" from our window
        while right in validator:
            # remove the very first element which is the repeating char
            validator.remove(s[left])
            # increment left pointer
            left += 1
        # keep adding the right character and update the result with the bigger number
        # comparing current result and current length of the validator set
        validator.add(right)
        res = max(res, len(validator))

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
