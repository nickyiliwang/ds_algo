from collections import Counter


def minWindow(s, t):
    left = 0
    needCount, haveCount = Counter(t), Counter()
    needLen, haveLen = len(t), 0
    res, resLen = "", len(t) + 1

    for right in range(len(s)):
        haveCount[s[right]] += 1

        if haveCount[s[right]] == needCount[s[right]]:
            haveLen += 1

        while haveLen == needLen:
            length = right - left + 1
            if length < resLen:
                res = s[left: right + 1]
                resLen = length

            haveCount[s[left]] -= 1
            if haveCount[s[left]] < needCount[s[left]]:
                haveLen -= 1

            left += 1

        right += 1

    return res

# Explanation
# Keys
# haveCount and needCount counter hash
# haveCount and needCount counts
# once and while haveLen == needLen we a haveCount window to reduce by moving the left pointer


def minWindow(s, t):
    if len(s) < len(t):
        return ""

    left = 0
    res = ""
    # resLen start infinite to have it shorter
    resLen = float("inf")
    need = Counter(t)
    have = Counter()
    needCounter = len(t)
    haveCounter = 0

    for right in range(len(s)):
        have[s[right]] += 1

        # we skip over char we don't need
        if have[s[right]] == need[s[right]]:
            haveCounter += 1

        while haveCounter == needCounter:
            # update result
            length = right - left + 1
            if length < resLen:
                # right index off by one
                res = s[left: right + 1]
                resLen = length

            # shorten window
            have[s[left]] -= 1
            if have[s[left]] < need[s[left]]:
                haveCounter -= 1

            left += 1

        right += 1

    return res


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
