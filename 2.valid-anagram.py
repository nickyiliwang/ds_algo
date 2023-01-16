# Quick idea:
def isAnagram(s, t):
    return sorted(s) == sorted(t)

# Using dictionary to implement (preferred)
# time O(s + t), space O(s + t)
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countA, countB = {}, {}

    for i in range(len(s)):
        # get method gets the key's value, if the key doesn't exit, return 0 as default
        # s[i] is the value we want to search, t[i] for countB
        countA[s[i]] = countA.get(s[i], 0) + 1
        countB[t[i]] = countB.get(t[i], 0) + 1

    for j in countA:
        # using get so no key error if the key doesn't exist
        if countA[j] != countB.get(j, 0):
            return False
    return True


s = "cat"
t = "rat"
print(isAnagram(s, t))

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
