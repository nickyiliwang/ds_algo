def characterReplacement(s, k):
    counter = Counter()
    left = 0
    res = 0
    for right in range(len(s)):
        counter[s[right]] += 1

        while (right - left + 1) - max(counter.values()) > k:
            counter[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


# we want the len of the window - max repeating number <= k


def characterReplacement(s, k):
    counter = Counter()
    left = 0
    res = 0
    for right in range(len(s)):
        counter[s[right]] += 1
        # if > k, out of bounds, while loop moving the left pointer to keep finding potential results
        while (right - left + 1) - max(counter.values()) > k:
            counter[s[left]] -= 1
            left += 1

        # we want the (length of the window (hence + 1), which will get us the remaining numbers that we need to replace
        #  (# to replace) - max repeating number) <= k , which is implied here
        # Meaning it's a potential result
        res = max(res, right - left + 1)

    return res


s = "AABABBA"
k = 1
characterReplacement(s, k)

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
