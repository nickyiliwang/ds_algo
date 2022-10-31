# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List


def longestCommonPrefix(strs: List[str]):
    res = ""

    # making sure we have a base range
    # looping each character index of first word
    for i in range(len(strs[0])):
        for w in strs:
            # if the index is equal to the length of word we are checking
            # then we know it's still inbound
            # if the i letter of each word does not match the first, return the current result
            if i == len(w) or w[i] != strs[0][i]:
                return res
        # else append each letter that passed the condition
        res += strs[0][i]

    return res


strs = ["flower", "flow", "flight"]

longestCommonPrefix(strs)
# print(longestCommonPrefix(strs))
