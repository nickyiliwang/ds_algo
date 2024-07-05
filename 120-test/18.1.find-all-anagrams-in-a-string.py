from collections import Counter


def findAnagrams(s, p):
    if len(s) < len(p):
        return []

    c1 = Counter(p)
    res = []
    window = len(p)

    c2 = Counter()

    for i in range(len(s)):
        if i < window:
            c2[s[i]] += 1
        else:
            c2[s[i - window]] -= 1
            c2[s[i]] += 1

        if c1 == c2:
            # here we appended the tail to c2 so the index is at the end of the window
            # window is length not index so to get the first index of the current window size, we add one after minus window.
            res.append(i - window + 1)

    return res


s = "cbaebabacd"
p = "abc"

findAnagrams(s, p)