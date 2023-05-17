from typing import *
from collections import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        left = 0
        needCount, haveCount = Counter(t), Counter()
        needLen, haveLen = len(t), 0
        res, resLen = "", float("inf")

        for right in range(len(s)):
            haveCount[s[right]] += 1

            if haveCount[s[right]] <= needCount[s[right]]:
                haveLen += 1

            while haveLen == needLen:
                if right - left + 1 < resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1

                haveCount[s[left]] -= 1
                if haveCount[s[left]] < needCount[s[left]]:
                    haveLen -= 1

                left += 1

        return res

# Method 2


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = Counter(t), Counter()
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
