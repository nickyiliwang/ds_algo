from typing import List
import os
os.system('clear')


def longestCommonPrefix(strs: List[str]):
    res = ""
    validator = strs[0]

    # making sure we have a base range
    # looping each character index of first word
    for i in range(len(validator)):
        for w in strs:
            # if the index is equal to the length of word we are checking
            # then we know it's still inbound
            # if the i letter of each word does not match the first, return the current result
            if i == len(w) or w[i] != validator[i]:
                return res
        # else append each letter that passed the condition
        res += validator[i]

    return res


strs = ["flower", "flow", "flight"]

print(longestCommonPrefix(strs))
