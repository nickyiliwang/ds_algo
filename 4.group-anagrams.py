from typing import List

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # sort first
    # one pass get val:index in hashMap
    # compare string
    hashMap = {}
    res = []

    for i, s in enumerate(strs):
        s = ''.join(sorted(s))
        if s in hashMap:
            hashMap[s] += [i]
        else:
            hashMap[s] = [i]

    print(hashMap)

    for x in hashMap:
        ana = []
        for y in hashMap[x]:
            ana.append(strs[y])
        res.append(ana)

    print(res)
    return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

groupAnagrams(strs)

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Notes
# 1. Tried to use ana = [] to get all occurence during the first pass
# 2. realized I might need an hashMap { x: [0,1,2] } a record of each repeated word: [index]
# 3. with this hashMap I'm still using a nested for loop, relative O(n^2) which is slow
